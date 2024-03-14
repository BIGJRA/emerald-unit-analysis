import json
from collections import defaultdict, Counter
from os import path

TM_SCORES = {
    "TM01": 31.3,  # Focus Punch - Route 115 w Surf
    "TM02": 44.2,  # Dragon Claw - Meteor Falls w Waterfall
    "TM03": 43.2,  # Water Pulse - Badge 8
    "TM04": 40.1,  # Calm Mind - Badge 7
    "TM05": 25.3,  # Roar - Route 114
    "TM06": 29.1,  # Toxic - Fiery Path w Strength
    "TM07": 37.1,  # Hail - Shoal Cave
    "TM08": 18.1,  # Bulk Up - Badge 2
    "TM09": 9.1,  # Bullet Seed - Route 104
    "TM10": 24.3,  # Hidden Power (R) - Slateport City after R111
    "TM11": 33.2,  # Sunny Day - Scorched Slab
    "TM12": 34.1,  # Taunt - Trick House Post Badge 6
    "TM13": 20.7,  # Ice Beam (R) - Game Corner or Abandoned Ship
    "TM14": 36.7,  # Blizzard - Lilycove Dept. Store
    "TM15": 36.8,  # Hyper Beam - Lilycove Dept. Store
    "TM16": 36.4,  # Light Screen - Lilycove Dept. Store
    "TM17": 36.1,  # Protect - Lilycove Dept. Store
    "TM18": 41.4,  # Rain Dance - Abandoned Ship w Dive
    "TM19": 35.1,  # Giga Drain - Route 123
    "TM20": 36.2,  # Safeguard - Lilycove Dept. Store
    "TM21": 39.1,  # Frustration (R) - Pacifidlog Town
    "TM22": 34.2,  # Solarbeam - Safari Zone
    "TM23": 44.1,  # Iron Tail - Meteor Falls w Waterfall
    "TM24": 20.6,  # Thunderbolt (R) - Game Corner or New Mauville
    "TM25": 36.6,  # Thunder - Lilycove Dept. Store
    "TM26": 42.1,  # Earthquake - Seafloor Cavern
    "TM27": 27.2,  # Return (R) - Fallarbor Town, Pacifidlog Town
    "TM28": 25.1,  # Dig - Route 114
    "TM29": 20.4,  # Psychic (R) - Game Corner or Victory Road
    "TM30": 34.4,  # Shadow Ball - Mt. Pyre
    "TM31": 41.2,  # Brick Break - Sootopolis City
    "TM32": 20.3,  # Double Team (R) - Game Corner, Route 113
    "TM33": 36.3,  # Reflect - Lilycove Dept. Store
    "TM34": 23.1,  # Shock Wave - Badge 3
    "TM35": 20.5,  # Flamethrower (R) - Game Corner
    "TM36": 31.6,  # Sludge Bomb - Dewford After Badge 5
    "TM37": 29.2,  # Sandstorm - Route 111 after Badge 4
    "TM38": 36.5,  # Fire Blast - Lilycove Dept. Store
    "TM39": 15.1,  # Rock Tomb - Badge 1
    "TM40": 33.3,  # Aerial Ace - Badge 6
    "TM41": 19.2,  # Torment - Slateport City
    "TM42": 31.1,  # Facade - Badge 5
    "TM43": 24.2,  # Secret Power (R) - Slateport City after R111
    "TM44": 35.2,  # Rest - Lilycove City
    "TM45": 22.1,  # Attract - Verdanturf Town
    "TM46": 19.1,  # Thief - Slateport City
    "TM47": 17.1,  # Steel Wing - Granite Cave
    "TM48": 34.3,  # Skill Swap - Mt. Pyre
    "TM49": 55.1,  # Snatch - S.S. Tidal (Postgame
    "TM50": 28.1,  # Overheat - Badge 8
    "HM01": 11.1,  # Cut - Rustboro City
    "HM02": 32.1,  # Fly - Route 119
    "HM03": 31.2,  # Surf - Badge 5
    "HM04": 24.1,  # Strength - Rusturf Tunnel w Rock Smash
    "HM05": 16.1,  # Flash - Granite Cave
    "HM06": 20.1,  # Rock Smash - Mauville City
    "HM07": 43.1,  # Waterfall - Sootopolis City Post Rayquaza
    "HM08": 41.1,  # Dive - Mossdeep City
}
TUTOR_SCORES = {
    "Double-Edge": 41.3,  # Sootopolis
    "DynamicPunch": 37.2,  # Mossdeep
    "Explosion": 39.2,  # Pacifidlog
    "Fury Cutter": 22.2,  # Verdanturf
    "Metronome": 25.2,  # Fallarbor
    "Mimic": 27.1,  # Lavaridge
    "Rollout": 20.2,  # Mauville
    "Sleep Talk": 32.2,  # Fortree
    "Substitute": 35.3,  # Lilycove
    "Swagger": 19.3  # Slateport
}
TM_SPLITS = {"TM13": 31.4, "TM24": 31.5, "TM32": 24.4, "TM29": 46.1}

def generate_text(pokemon_names):
    lines = []
    first_mon = pokemon_names[0].capitalize()
    lines.append(f"# Pokemon Emerald Unit Feel Analysis: {first_mon} line\n")
    lines.append(f"{first_mon} is a TODO type Pokemon, first obtained at TODO. Its ability is TODO. It evolves at TODO, then again at "
                 f"TODO.\n")
    lines.append('### Base Stats\n')
    for mon in pokemon_names:
        j = get_json(mon)["stats"]
        total = sum([int(j[stat]) for stat in ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]])
        lines.append(
            f"{mon.capitalize()}: **{j["HP"]}** HP / **{j["Attack"]}** Atk / **{j["Defense"]}** Def / **{j["Sp. Atk"]}** SpA / **{j["Sp. Def"]}** SpD / **{j["Speed"]}** Spe (**{total}** BST)\n")

    lines.append('### Moveset\n')

    acq, data = get_learnset_and_move_data(pokemon_names)

    move_lines = [['Acquisition', '---'], ['Move', '---'], ['Type', '---'], ['Power', '---'], ['Accuracy', '---'],
                  ['PP', '---'], ['Notes'.ljust(25), '---']]
    for move in acq:
        score = move[0]
        n = move[1]
        type, pwr, acc, pp = data[n]["Type"], data[n]["Pwr"], data[n]["Acc"], data[n]["PP"]
        notes = ''
        if 'Tutor' in move[2]: notes = "Emerald only"
        if any(TM in move[2] for TM in TM_SPLITS | {"TM35": 20.5}) and 20 < score < 21: # Checks for specifically game corner stuff:
            notes = 'Buy at Game Corner'
        for idx, thing in enumerate([f'{move[2]}', f'{n}', f'{type}', f'{pwr}', f'{acc}', f'{pp}', f'{notes}']):
            move_lines[idx].append(thing)
    lengths = [max([len(s) for s in group]) for group in move_lines]
    for pos in range(len(move_lines[0])):
        curr = "|" + "|".join([thing[pos].ljust(lengths[idx]) for idx, thing in enumerate(move_lines)]) + "|"
        lines.append(curr)

    lines.append('')
    lines.append("### Analysis")
    return '\n'.join(lines)


def get_learnset_and_move_data(pokemon_names):
    acq = defaultdict(lambda: [None for _ in range(len(pokemon_names))])
    move_data = {}
    curr = -1
    for p in pokemon_names:
        curr += 1
        j = get_json(p)["moves"]
        for m in j:
            move_data[m["Move"]] = m
            if m["LearnType"] == "LevelingUp":
                try:
                    acq[(m["Move"], m["LearnType"])][curr] = (int(m["Level"]), f"Lv. {m["Level"]}")
                except KeyError:  # Some movesets are constructed with "RSE" as the key instead of "Level"
                    if m["RSE"] == "N/A": continue
                    acq[(m["Move"], m["LearnType"])][curr] = (int(m["RSE"]), f"Lv. {m["RSE"]}")
            elif m["LearnType"] == "TmHm":
                acq[(m["Move"], m["LearnType"])][curr] = (TM_SCORES[m['TM']], f"{m['TM']}")
            elif m["LearnType"] == "Tutoring":
                if m["Move"] not in TUTOR_SCORES: continue
                acq[(m["Move"], m["LearnType"])][curr] = (TUTOR_SCORES[m['Move']], "Tutor")
    acq_list = []
    for a in acq:
        move, _learntype = a
        entries = acq[a]
        if (len(entries) == 3 and entries[0] == entries[1] == entries[2]) or (
                len(entries) == 2 and entries[0] == entries[1]):
            learn_str = entries[0][1]
        else:
            learn_str = ' / '.join([e[1] if e is not None else '--' for e in entries])
        if "TM49" in learn_str: continue # skip Snatch, which is postgame
        score = max([e[0] if e is not None else -1 for e in entries])

        acq_list.append((score, move, learn_str))

        for entry in set(entries):
            if entry is not None and entry[1] in TM_SPLITS:
                acq_list.append((TM_SPLITS[entry[1]], move, learn_str))
    acq_list.sort()
    return acq_list, move_data


def get_json(pokemon_name):
    with open(path.join('data', f'{pokemon_name}_3.json')) as f:
        j = json.loads(f.read())
    return j


def write_analysis(text, pokemon_names):
    hi = pokemon_names[-1].lower()
    with open(path.join('templates', f'{hi}.md'), 'w+') as f:
        f.write(text)


if __name__ == "__main__":
    with open('lines.txt', 'r') as f:
        for line in f.readlines():
            mons = line.replace('\n', '').split(',')
            print(f"Creating template for {mons[-1]} line...")
            t = generate_text(mons)
            write_analysis(t, mons)
            print(f"Created template for {mons[-1]} line!")
