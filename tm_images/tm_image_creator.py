from os import path

from PIL import Image, ImageDraw, ImageFont

def createImage(tm_string, move, type, show=False):

    img = Image.open(path.join('raw', f'TM - {type.capitalize()}.png'))

    size = img.size

    W = H = size[0] * 10
    img = img.resize((W, H))
    img.putalpha(155)

    font1 = ImageFont.truetype("pokemonemerald.ttf", size=260)
    font2 = ImageFont.truetype("pokemonemerald.ttf", size=105)

    draw = ImageDraw.Draw(img)

    draw.text((0.5 * W, 0.49 * H), anchor="ms", text=tm_string, fill=(255, 255, 255), font=font1)
    draw.text((0.5 * W, 0.73 * H), anchor="ms", text=move, fill=(255, 255, 255), font=font2)

    if show:
        img.show()

    img.save(path.join('tm', f'{tm_string}.png'))

l = {
    "TM01": ("Focus Punch", "Fighting"),
    "TM02": ("Dragon Claw", "Dragon"),
    "TM03": ("Water Pulse", "Water"),
    "TM04": ("Calm Mind", "Psychic"),
    "TM05": ("Roar", "Normal"),
    "TM06": ("Toxic", "Poison"),
    "TM07": ("Hail", "Ice"),
    "TM08": ("Bulk Up", "Fighting"),
    "TM09": ("Bullet Seed", "Grass"),
    "TM10": ("Hidden Power", "Normal"),
    "TM11": ("Sunny Day", "Fire"),
    "TM12": ("Taunt", "Dark"),
    "TM13": ("Ice Beam", "Ice"),
    "TM14": ("Blizzard", "Ice"),
    "TM15": ("Hyper Beam", "Normal"),
    "TM16": ("Light Screen", "Psychic"),
    "TM17": ("Protect", "Normal"),
    "TM18": ("Rain Dance", "Water"),
    "TM19": ("Giga Drain", "Grass"),
    "TM20": ("Safeguard", "Normal"),
    "TM21": ("Frustration", "Normal"),
    "TM22": ("Solarbeam", "Grass"),
    "TM23": ("Iron Tail", "Steel"),
    "TM24": ("Thunderbolt", "Electric"),
    "TM25": ("Thunder", "Electric"),
    "TM26": ("Earthquake", "Ground"),
    "TM27": ("Return", "Normal"),
    "TM28": ("Dig", "Ground"),
    "TM29": ("Psychic", "Psychic"),
    "TM30": ("Shadow Ball", "Ghost"),
    "TM31": ("Brick Break", "Fighting"),
    "TM32": ("Double Team", "Normal"),
    "TM33": ("Reflect", "Psychic"),
    "TM34": ("Shock Wave", "Electric"),
    "TM35": ("Flamethrower", "Fire"),
    "TM36": ("Sludge Bomb", "Poison"),
    "TM37": ("Sandstorm", "Rock"),
    "TM38": ("Fire Blast", "Fire"),
    "TM39": ("Rock Tomb", "Rock"),
    "TM40": ("Aerial Ace", "Flying"),
    "TM41": ("Torment", "Dark"),
    "TM42": ("Facade", "Normal"),
    "TM43": ("Secret Power", "Normal"),
    "TM44": ("Rest", "Psychic"),
    "TM45": ("Attract", "Normal"),
    "TM46": ("Thief", "Dark"),
    "TM47": ("Steel Wing", "Steel"),
    "TM48": ("Skill Swap", "Psychic"),
    "TM49": ("Snatch", "Dark"),
    "TM50": ("Overheat", "Fire"),
    "HM01": ("Cut", "Normal"),
    "HM02": ("Fly", "Flying"),
    "HM03": ("Surf", "Water"),
    "HM04": ("Strength", "Normal"),
    "HM05": ("Flash", "Normal"),
    "HM06": ("Rock Smash", "Fighting"),
    "HM07": ("Waterfall", "Water"),
    "HM08": ("Dive", "Water"),
}

for tm, (move, type) in l.items():
    createImage(tm, move, type)
    print(f'Created image for {tm}')

