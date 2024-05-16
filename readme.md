# Pokemon Emerald Unit Analysis

This is a repository for my analysis [writeups](https://github.com/BIGJRA/emerald-unit-analysis/tree/main/writeups) on (eventually) every line of Pokemon in Emerald Version. 

To use or modify my utility scripts, clone the repository and run the python files in the root corresponding to what you're looking to do.

## Analysis Philosophy

In this series, I intend to look into every single line of Pokemon in the Gen. III Hoenn Pokedex and discuss their “unit feel” across normal gameplay in Ruby, 

I have been playing every Pokémon game, starting with Ruby and playing all the way to Violet. These games captured me at age 6 but even at age 24, I find myself enamored by these games and its wonderful world of creatures. I completed a Living Dex up to gen 8 before burning out in gen 9 as well, so I’ve had at least some experience training up most of the Pokemon in the series. I’ve also played numerous Pokemon fangames and ROM hacks that experiment with the formula (if you recognize my username you might also recognize the in-depth guides I’ve written for Pokemon Reborn and Pokemon Rejuvenation, for example).

However, I realized a few years ago that I had become somewhat disillusioned with Pokemon games. Without toggleable Exp. Share and Set Mode, non-reusable TMs, and a considered, linear story, the newer games just aren't doing it for me. After taking a break from Pokemon for a few years and getting really into other RPG’s like Fire Emblem, I came back to the Pokemon series, replaying games from Gen 1-5, hoping to really pay attention to the strengths of the series that have afforded it its endurance and popularity over time.

This isn’t a post about my opinions on recent generations however – I mention this just to highlight the positives of what I think is a brilliant core gameplay loop established in Gen 1 that has continued throughout the series. Pokemon is a simple formula: as you explore the world, you get access to numerous new Pokemon that you can choose to use in your team. Along this journey you fight other trainers as you build your team, hoping to defeat the champion. You get to choose Pokemon that you like – maybe you’ll build a balanced team, or maybe you’ll pick favorites. Your team choices can be to fill a short term role for specific fights or long term roles in a team. With never fewer than 150 Pokemon in a regional dex per game, the player is allowed to experiment endlessly on replays by using new Pokemon!

Yet you’re still confined by the relative space afforded to you by the game at any point. You only have these lines: a starter, Pidgey, Rattata, Caterpie, Weedle, Spearow, Nidoran M/F, and Pikachu to defeat Brock in Gen 1. You have access to almost every Pokemon to fight the Elite Four, and by this point they’ve gotten better moves and you have more options with TM’s. Each sequence of the game is like a puzzle, but you get to choose from a bag the pieces that you will use to solve it. This basic idea forms the foundation that makes Pokemon so fun to replay for me personally and what motivated me to talk about how each Pokemon line feels to use, from the moment it is available to beating the champion (game's climax).

What is “unit feel”? In the Fire Emblem community, YouTuber Professor Bopper describes this term as the following: “how good a character is at telling a unique, dramatic gameplay story to make them feel more exciting or interesting.” See his video here for an overview of the term as it relates to Fire Emblem: https://youtu.be/RJIofIwVH2w?si=raXIhweIyGb63UZQ

I think this term can translate to Pokemon fairly easily – how good is the Pokemon line at telling a story as a party member as you play through the game? As we’ll get into with the first few entries, this means that starter Pokemon generally have some of the best unit feel. Unlike something like Roy in FE6 – your first character with perfect “availability” in Pokemon almost always will be good at telling a dramatic gameplay story thanks to its strong stats, two evolutions that help it spike in power, good movesets in almost every case, and ability to gain EXP quickly and snowball. On the flip side, I think something like Chimecho in Gen. III has somewhat poor unit feel. It doesn’t get to evolve, it is rare and obtained really late into the game, and it doesn’t really stand out meaningfully or have any niches that aren’t covered by Gardevoir or Alakazam, for example.

One other thing that I should bring up is that I will NOT be ranking Pokemon or directly trying to state how “good” they are. I’m much more interested in the story that a Pokemon can tell as a member of the team, but there is regardless going to be significant overlap. In general being available earlier, having access to moves and strategies that aren’t as widely available, relatively unique typings, notable stats and abilities, the potential for evolution, and things of this nature are generally what is on my mind when thinking about unit feel for Pokemon, but it’s really subjective at the end of the day. 

Frankly, Pokemon as a game series commits to too many goals. On one hand is the original motto "Gotta Catch 'Em All"; it is a game with a numbered list, nudging players to embark on the long and expensive (and sometimes LITERALLY IMPOSSIBLE if you’re going for mythicals) journey to collect them all. The gameplay itself is a simultaneous hybrid of a PVE RPG, PVP competitive game, and monster collection game, all of which are very fundamentally different experiences and require very different skills. A focus strictly on the RPG gameplay from start to finish is therefore considered here - older Pokemon games definitely are worth it to play and replay just for this PVE RPG gameplay alone.

I am going to be considering Pokemon as “units” in the RPG game: generally from the earliest point in the game you could add them to your team, up until you’ve completed the story content of the game. I will not be discussing how well they fare in competitive nor battle facility contexts here. In general, what’s “reasonable” for a in-game run through Pokemon will be level-up moves, choice of ability, TM moves that are obtainable in the game, tutor moves, and move relearner moves. Held items obtainable through normal gameplay are fine to discuss if they’re notable as well. Since egg moves are entirely obscured from the player and almost always force a Pokemon to be stuck behind in Exp due to breeding, I won’t generally consider egg moves, though I am interested in them in concept. After basically looking at all the options a Pokemon has over the course of the game, the next task will be to look at how these options might fare against the story fights of the game, not from an "efficient" planned run perspective, but from a unit feel one. 

Why Pokemon Emerald? I like it, and I've played it a ton of times, really. The lack of the Physical/Special split should give us things to talk about. Movesets are also not too huge at this point in time, so the minutiae should be more interesting. I think there are interesting analyses to be made of the other 2D Pokemon games (at least) but I decided to roll with Emerald (and Ruby/Sapphire, when necessary) for now.

## Rules 

Here’s the thing about Pokemon – you can literally overlevel one Pokemon like a starter and have 1 guy who covers its weaknesses and win everything. You can also easily buy things like X Attack, Revive, and Full Restores to blast through the games. If we assume that these things are in play, discussions of attributes of Pokemon are largely reductive since any Pokemon can be given insane stats and sweep almost anything. Aside from a weak attempt, Pokemon has never strived for robust difficulty options, so we have to do some of the hard work in establishing rules to make discussion of units interesting. Feel free to play Pokemon how you like of course, but for my discussion, some “rules” I am going by: 

- **Set mode is on.** Unit feel of tanky Pokemon that can be switched in doesn’t matter if you can always have an advantageous matchup.
- **Hardcore ~~Nuzlocke~~ Level Caps.** I am going to take the “Hardcore” from “Hardcore Nuzlocke” – analysis will be conducted as if your Pokemon are never exceeding the next gym leader’s (or Champion’s, with 8 badges) highest level Pokemon. I.e. Lv. 15 for Roxanne, Lv. 18 for Brawly. Knowing that Torchic will not be evolved when it fights Roxanne makes it simple, and discussion of the fight more interesting.
- **No Nuzlocke play - fainting is allowed.** I don’t enjoy Nuzlockes (nor the Rare Candy grind that comes with it).
- **No items from the bag in battle**. If any Pokemon can raise its stats, recover HP, or get revived anytime, fewer moves and strategies are interesting.
- **Full team of six Pokemon is used**. This kinda goes with the level cap thing but I am assuming the player uses a full team of six Pokemon. This allows discussion of how a Pokemon can fit into a full team.
- **No trading with other games**. This means I won't for example trade an Absol in to use on Roxanne, considering it only as it appears around the sixth badge, nor trade in infinite copies of TM Earthquake. Trading evolutions are kind of a mess, but since I do want to talk about things like Machamp I will allow them (assuming trade-tradebacks). 
- **Grinding levels by way of repeatable trainers or wild Pokemon is allowed, but discouraged.** If a Pokemon needs to be grinded a bit for a zero-to-hero arc, that is arguably part of its unit story, but in general I play where I fight all the trainers in the game without rematches and only fight wild Pokemon when they appear while exploring.

## Progress

- [ ] Treecko, Grovyle, Sceptile
- [x] Torchic, Combusken, Blaziken
- [x] Mudkip, Marshtomp, Swampert
- [ ] Poochyena, Mightyena
- [ ] Zigzagoon, Linoone
- [x] Wurmple, Silcoon, Beautifly
- [x] Wurmple, Cascoon, Dustox
- [x] Lotad, Lombre, Ludicolo
- [x] Seedot, Nuzleaf, Shiftry
- [x] Taillow, Swellow
- [ ] Wingull, Pelipper
- [ ] Ralts, Kirlia, Gardevoir
- [x] Surskit, Masquerain
- [ ] Shroomish, Breloom
- [x] Slakoth, Vigoroth, Slaking
- [x] Abra, Kadabra, Alakazam
- [x] Nincada, Ninjask
- [ ] Nincada, Shedinja
- [ ] Whismur, Loudred, Exploud
- [ ] Makuhita, Hariyama
- [ ] Goldeen, Seaking
- [ ] Magikarp, Gyarados
- [x] Azurill, Marill, Azumarill
- [ ] Geodude, Graveler, Golem
- [x] Nosepass
- [ ] Skitty, Delcatty
- [x] Zubat, Golbat, Crobat
- [ ] Tentacool, Tentacruel
- [x] Sableye
- [x] Mawile
- [x] Aron, Lairon, Aggron
- [ ] Machop, Machoke, Machamp
- [x] Meditite, Medicham
- [ ] Electrike, Manectric
- [x] Plusle / Minun
- [ ] Magnemite, Magneton
- [ ] Voltorb, Electrode
- [ ] Volbeat
- [ ] Illumise
- [ ] Oddish, Gloom, Vileplume
- [x] Oddish, Gloom, Bellossom
- [ ] Doduo, Dodrio
- [x] Roselia
- [ ] Gulpin, Swalot
- [ ] Carvanha, Sharpedo
- [x] Wailmer, Wailord
- [ ] Numel, Camerupt
- [x] Slugma, Magcargo
- [x] Torkoal
- [ ] Grimer, Muk
- [ ] Koffing, Weezing
- [ ] Spoink, Grumpig
- [x] Sandshrew, Sandslash
- [ ] Spinda
- [ ] Skarmory
- [ ] Trapinch, Vibrava, Flygon
- [x] Cacnea, Cacturne
- [ ] Swablu, Altaria
- [x] Zangoose
- [x] Seviper
- [ ] Lunatone
- [x] Solrock
- [ ] Barboach, Whiscash
- [ ] Corphish, Crawdaunt
- [ ] Baltoy, Claydol
- [ ] Lileep, Cradily
- [ ] Anorith, Armaldo
- [ ] Igglybuff, Jigglypuff, Wigglytuff
- [ ] Feebas, Milotic
- [ ] Castform
- [x] Staryu, Starmie
- [ ] Kecleon
- [ ] Shuppet, Banette
- [x] Duskull, Dusclops
- [x] Tropius
- [ ] Chimecho
- [ ] Absol
- [ ] Vulpix, Ninetales
- [ ] Pichu, Pikachu, Raichu
- [x] Psyduck, Golduck
- [x] Wynaut, Wobbuffet
- [ ] Natu, Xatu
- [ ] Girafarig
- [ ] Phanpy, Donphan
- [ ] Pinsir
- [ ] Heracross
- [x] Rhyhorn, Rhydon
- [ ] Snorunt, Glalie
- [ ] Spheal, Sealeo, Walrein
- [ ] Clamperl, Huntail
- [ ] Clamperl, Gorebyss
- [x] Relicanth
- [ ] Corsola
- [x] Chinchou, Lanturn
- [x] Luvdisc
- [ ] Horsea, Seadra, Kingdra
- [x] Bagon, Shelgon, Salamence
- [ ] Beldum, Metang, Metagross
- [ ] Regirock
- [ ] Regice
- [ ] Registeel
- [ ] Latias
- [ ] Latios
- [ ] Kyogre
- [ ] Groudon
- [ ] Rayquaza