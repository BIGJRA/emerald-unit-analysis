import simplejson
from os import path

from bs4 import BeautifulSoup, Stylesheet
import roman
import requests


def getPokemonMovesetURL(pokemon_name, gen_number=3):
    return f'https://bulbapedia.bulbagarden.net/wiki/{pokemon_name.capitalize()}_(Pok%C3%A9mon)/Generation_{roman.toRoman(gen_number)}_learnset#By_leveling_up'

def getPokemonMainURL(pokemon_name):
    return f'https://bulbapedia.bulbagarden.net/wiki/{pokemon_name.capitalize()}_(Pok%C3%A9mon)'

def getHTMLMoveDataFilepath(pokemon_name, gen_number=3):
    return path.join('data', f'{pokemon_name.lower()}_moves_{gen_number}.html')

def getHTMLMainDataFilepath(pokemon_name, gen_number=3):
    return path.join('data', f'{pokemon_name.lower()}_main_{gen_number}.html')

def getJSONDataFilepath(pokemon_name, gen_number=3):
    return path.join('data', f'{pokemon_name.lower()}_{gen_number}.json')

def saveMoveContents(pokemon_name, gen_number=3):
    contents = requests.get(getPokemonMovesetURL(pokemon_name, gen_number)).content
    with open(getHTMLMoveDataFilepath(pokemon_name, gen_number), 'w+') as f:
        f.write(str(contents))

def saveMainContents(pokemon_name):
    contents = requests.get(getPokemonMainURL(pokemon_name)).content
    with open(getHTMLMainDataFilepath(pokemon_name), 'w+') as f:
        f.write(str(contents))

def extractMoveData(pokemon_name, gen_number=3):
    data = []
    with open(getHTMLMoveDataFilepath(pokemon_name, gen_number), 'r') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    for title_block in soup.find_all('h4'):
        # gets the title of the kind of move - will become a key
        # ie. LevelingUp, TmHm, Breeding, Tutoring, APriorEvolution
        title_text = title_block.findNext('span').get('id')
        title_text = ''.join(x for x in title_text.title() if not x in (' ', '_', '/'))
        title_text = title_text[2:] if title_text[:2] in ["By"] else title_text
        title_text = title_text.replace("Tm.2Fhm", "TmHm") # hard fix since bulbapedia changed

        # skip events and shadow moves
        if title_text in ["SpecialMoves", "Events"]: continue

        # Find the table after the label
        next_table = title_block.findNextSibling('table')

        # Addresses weird cases like Mew where there's a separate table containing
        # The main one that simply tells you that it gets all the TMs.
        if "expandable" in next_table.attrs.get("class", []):
            next_table = next_table.find_next('table')

        # Level up table is sortable and handled differently - finds header and gets rows
        if title_text == "LevelingUp":
            for sub in next_table.find_all('table'):
                if "Move" in sub.find('tr').text:
                    rows = sub.find_all('tr')

        # Other tables are more standard - find the header and get all the rows after
        else:
            for h_row in next_table.find_all('tr'):
                if "Move" in h_row.text:
                    break
            rows = [h_row] + list(filter(lambda x: x != r'\n', h_row.next_siblings))

        for row in rows:
            skip = False
            row_data = []
            cells = row.find_all(['td', 'th'])

            for cell in cells:
                # Skips the rows at the bottom that aren't move data, skips completely empty groups
                if cell.attrs.get("class") is not None and cell.attrs.get("class")[0] == "roundybottom" or "learns no" in cell.text or "has no" in cell.text:
                    skip = True
                    break

                raw = cell.find(string=True, recursive=False).strip() if cell.find('span',{'style': 'display:none'}) else cell.get_text(strip=True).replace(r'\n', '').strip()

                #handles tutor game availability stuff
                if raw in ["FR", "LG", "E", "XD"]:
                    if cell.attrs.get("style") is not None and "#FFFFFF" in cell.attrs.get("style"):
                        raw = ''

                row_data.append(raw.replace('\\n','').replace('\\xe2\\x80\\x94','--').replace('.','').replace('*',''))
            if skip:
                continue

            # Labels first so it can zip them
            if "Move" in row_data:
                labels = row_data

            else:
                # Skips cell where the TM graphic is
                if title_text == "TmHm":
                    row_data = row_data[1:]

                # Combines all tutor games into one string
                if title_text == "Tutoring":
                    row_data = [''.join(row_data[:4])] + row_data[4:]

                data.append({l: r for l, r in zip(labels, row_data) if l not in ("Contest", "Appeal", "Jamming")} | {"LearnType": title_text})
    return data

def extractStatData(pokemon_name):
    data = {}
    with open(getHTMLMainDataFilepath(pokemon_name), 'r') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    table = soup.find(id=["Base_stats","Stats"]).find_next("table")
    headers = table.find_all("th")
    for header in headers:
        if not header.find('a'): continue
        url = header.find('a').attrs['href']
        if "HP" not in url and "#" not in url: continue
        h_text = header.text.replace('\\n','')
        data[h_text.split(':')[0]] = h_text.split(':')[1]
    return data

def extractAllData(pokemon_name, gen_number=3, dex_number = None):
    moves = extractMoveData(pokemon_name, gen_number=gen_number)
    stats = extractStatData(pokemon_name)
    data = {"moves": moves, "stats": stats, "dex_number": dex_number}
    with open(getJSONDataFilepath(pokemon_name, gen_number), 'w') as f:
        f.write(simplejson.dumps(data, indent=4))

if __name__ == '__main__':
    with open('mons.txt') as f:
        mons = f.read().split('\n')
    for num, mon in enumerate(mons):
        print(f"Getting data for {mon}...")
        # if mon != "Kyogre": continue
        saveMoveContents(mon)
        saveMainContents(mon)
        extractAllData(mon, dex_number=num + 1)
        print(f"Completed getting data for {mon}!")

