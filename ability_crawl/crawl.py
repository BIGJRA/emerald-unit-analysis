import os

from bs4 import BeautifulSoup
import requests

PSYPOKES_URL = 'http://www.psypokes.com/rsefrlg/abilities.php'

soup = BeautifulSoup(requests.get(PSYPOKES_URL).content, 'html.parser')
abilities = {}

table = soup.find(name="table", attrs={"class": "psypoke"})
r = table.find_next('tr')
while True:
    r = r.find_next('tr')
    if 'class' in r.attrs:
        break
    tds = r.find_all('td')
    name = tds[0].text
    mons = tds[2].text.split(', ')
    abilities[name] = mons

def strip_non_hoenn_dex(abilities_dict):

    def mon_in_hoenn(mon):
        with open(os.path.join(os.pardir, 'mons.txt')) as f:
            return mon in f.read()

    new = {}
    for move, mon_list in abilities_dict.items():
        new[move] = list(filter(mon_in_hoenn, mon_list))

    return new

print(*[f"{a[0]} {a[1]}" for a in abilities.items()], sep='\n')
stripped = strip_non_hoenn_dex(abilities)
print(*[f"{a[0]} {a[1]}" for a in stripped.items()], sep='\n')
