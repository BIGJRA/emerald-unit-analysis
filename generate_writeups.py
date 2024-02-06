import json
from collections import defaultdict, Counter
from os import path

TM_SCORES = {
    "TM01": 31,  # Focus Punch - Route 115 w Surf
    "TM02": 44,  # Dragon Claw - Meteor Falls w Waterfall
    "TM03": 43,  # Water Pulse - Badge 8
    "TM04": 40,  # Calm Mind - Badge 7
    "TM05": 25,  # Roar - Route 114
    "TM06": 29,  # Toxic - Fiery Path w Strength
    "TM07": 37,  # Hail - Shoal Cave
    "TM08": 18,  # Bulk Up - Badge 2
    "TM09": 9,  # Bullet Seed - Route 104
    "TM10": 24,  # Hidden Power (R) - Slateport City after R111
    "TM11": 33,  # Sunny Day - Scorched Slab
    "TM12": 34,  # Taunt - Trick House Post Badge 6
    "TM13": 20,  # Ice Beam (R) - Game Corner or Abandoned Ship
    "TM14": 36,  # Blizzard - Lilycove Dept. Store
    "TM15": 36,  # Hyper Beam - Lilycove Dept. Store
    "TM16": 36,  # Light Screen - Lilycove Dept. Store
    "TM17": 36,  # Protect - Lilycove Dept. Store
    "TM18": 41,  # Rain Dance - Abandoned Ship w Dive
    "TM19": 35,  # Giga Drain - Route 123
    "TM20": 36,  # Safeguard - Lilycove Dept. Store
    "TM21": 39,  # Frustration (R) - Pacifidlog Town
    "TM22": 34,  # Solarbeam - Safari Zone
    "TM23": 44,  # Iron Tail - Meteor Falls w Waterfall
    "TM24": 20,  # Thunderbolt (R) - Game Corner or New Mauville
    "TM25": 36,  # Thunder - Lilycove Dept. Store
    "TM26": 42,  # Earthquake - Seafloor Cavern
    "TM27": 27,  # Return (R) - Fallarbor Town, Pacifidlog Town
    "TM28": 25,  # Dig - Route 114
    "TM29": 20,  # Psychic (R) - Game Corner or Victory Road
    "TM30": 34,  # Shadow Ball - Mt. Pyre
    "TM31": 41,  # Brick Break - Sootopolis City
    "TM32": 20,  # Double Team (R) - Game Corner, Route 113
    "TM33": 36,  # Reflect - Lilycove Dept. Store
    "TM34": 23,  # Shock Wave - Badge 3
    "TM35": 20,  # Flamethrower (R) - Game Corner
    "TM36": 31,  # Sludge Bomb - Dewford After Badge 5
    "TM37": 29,  # Sandstorm - Route 111 after Badge 4
    "TM38": 36,  # Fire Blast - Lilycove Dept. Store
    "TM39": 15,  # Rock Tomb - Badge 1
    "TM40": 33,  # Aerial Ace - Badge 6
    "TM41": 20,  # Torment - Slateport City
    "TM42": 33,  # Facade - Badge 5
    "TM43": 24,  # Secret Power (R) - Slateport City after R111
    "TM44": 36,  # Rest - Lilycove City
    "TM45": 22,  # Attract - Verdanturf Town
    "TM46": 20,  # Thief - Slateport City
    "TM47": 17,  # Steel Wing - Granite Cave
    "TM48": 34,  # Skill Swap - Mt. Pyre
    "TM49": 55,  # Snatch - S.S. Tidal (Postgame
    "TM50": 28,  # Overheat - Badge 8
    "HM01": 11,  # Cut - Rustboro City
    "HM02": 32,  # Fly - Route 119
    "HM03": 31,  # Surf - Badge 5
    "HM04": 24,  # Strength - Rusturf Tunnel w Rock Smash
    "HM05": 16,  # Flash - Granite Cave
    "HM06": 21,  # Rock Smash - Mauville City
    "HM07": 43,  # Waterfall - Sootopolis City Post Rayquaza
    "HM08": 41,  # Dive - Mossdeep City
}
TUTOR_SCORES = {
    "Double-Edge": 41,  # Sootopolis
    "DynamicPunch": 37,  # Mossdeep
    "Explosion": 39,  # Pacifidlog
    "Fury Cutter": 22,  # Verdanturf
    "Metronome": 25,  # Fallarbor
    "Mimic": 27,  # Lavaridge
    "Rollout": 21,  # Mauville
    "Sleep Talk": 32,  # Fortree
    "Substitute": 36,  # Lilycove
    "Swagger": 20  # Slateport
}

def generate_text(pokemon_names):
    lines = []
    first_mon = pokemon_names[0].capitalize()
    lines.append(f"# Pokemon Emerald Unit Feel Analysis: {first_mon} line\n")
    lines.append(f"{first_mon} is first obtained at TODO. It's ability is TODO. It evolves at TODO, then again at TODO.\n")
    lines.append('### Base Stats\n')
    for mon in pokemon_names:
        j = get_json(mon)["stats"]
        lines.append(f"{mon.capitalize()}: **{j["HP"]}** HP / **{j["Attack"]}** Atk / **{j["Defense"]}** Def / **{j["Sp. Atk"]}** SpA / **{j["Sp. Def"]}** SpD / **{j["Speed"]}** Spe\n")

    lines.append('### Moveset\n')

    acq, data = get_learnset_and_move_data(pokemon_names)

    move_lines = [['Acquisition','---'], ['Move','---'], ['Type','---'], ['Power','---'], ['Accuracy','---'], ['PP','---'],['Notes'.ljust(25), '---']]
    for move in acq:
        n = move[1]
        type, pwr, acc, pp = data[n]["Type"], data[n]["Pwr"], data[n]["Acc"], data[n]["PP"]
        notes = ''
        if 'Tutor' in move[2]: notes = "Emerald only"
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
                except KeyError: # Some movesets are constructed with "RSE" as the key instead of "Level"
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
        if (len(entries) == 3 and entries[0] == entries[1] == entries[2]) or (len(entries) == 2 and entries[0] == entries[1]):
            learn_str = entries[0][1]
        else:
            learn_str = ' / '.join([e[1] if e is not None else '--' for e in entries])
        score = max([e[0] if e is not None else -1 for e in entries])

        # Handles final stage Lv. 1 moves - might as well put them at the Move Relearner - Fallarbor @ Lv. 25
        if learn_str in ['-- / -- / Lv. 1', '-- / Lv. 1']:
            print(move, pokemon_names)
            score = 25
        acq_list.append((score, move, learn_str))
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
            mons = line.replace('\n','').split(',')
            print(f"Creating template for {mons[-1]} line...")
            t = generate_text(mons)
            write_analysis(t, mons)
            print(f"Created template for {mons[-1]} line!")