import csv
import pypokedex


class Move:
    def __init__(self, name, moveType, power, accuracy):
        self.name = name
        self.moveType = moveType
        self.power = power
        self.accuracy = accuracy


class Pokemon:
    def __init__(self, name, level, hpEV, atkEV, defEV, spaEV, spdEV, speEV, hpIV, atkIV, defIV, spaIV, spdIV, speIV):
        self.name = name
        self.level = level
        self.hpE = hpEV
        self.hpI = hpIV
        self.atkE = atkEV
        self.atkI = atkIV
        self.defE = defEV
        self.defI = defIV
        self.spaE = spaEV
        self.spaI = spaIV
        self.spdE = spdEV
        self.spdI = spdIV
        self.speE = speEV
        self.speI = speIV
        self.pokemon = pypokedex.get(name=self.name)
        self.types = pokemon.types


bannedMoves = ["After You", "Apple Acid", "Armor Cannon", "Assist", "Astral Barrage", "Aura Wheel", "Baneful Bunker",
               "Beak Blast", "Behemoth Bash", "Behemoth Blade", "Belch", "Bestow", "Blazing Torque", "Body Press",
               "Branch Poke", "Breaking Swipe", "Celebrate", "Chatter", "Chilling Water", "Chilly Reception",
               "Clangorous Soul", "Collision Course", "Combat Torque", "Comeuppance", "Copycat", "Counter", "Covet",
               "Crafty Shield", "Decorate", "Destiny Bond", "Detect", "Diamond Storm", "Doodle", "Double Iron Bash",
               "Double Shock", "Dragon Ascent", "Dragon Energy", "Drum Beating", "Dynamax Cannon", "Electro Drift",
               "Endure", "Eternabeam", "False Surrender", "Feint", "Fiery Wrath", "Fillet Away", "Fleur Cannon",
               "Focus Punch", "Follow Me", "Freeze Shock", "Freezing Glare", "Glacial Lance", "Grav Apple",
               "Helping Hand", "Hold Hands", "Hyper Drill", "Hyperspace Fury", "HyperSspace Hole", "Ice Burn",
               "Instruct", "Jet Punch", "Jungle Healing", "Kings Shield", "Life Dew", "Light of Ruin", "Make It Rain",
               "Magical Torque", "Mat Block", "Me First", "Meteor Assault", "Mimic", "Mind Blown", "Mirror Coat",
               "Mirror Move", "Moongeist Beam", "Nature Power", "Natures Madness", "Noxious Torque", "Obstruct",
               "Order Up", "Origin Pulse", "Overdrive", "Photon Geyser", "Plasma Fists", "Population Bomb", "Pounce",
               "Power Shift", "Precipice Blades", "Protect", "Pyro Ball", "Quash", "Quick Guard", "Rage Fist",
               "Rage Powder", "Raging Bull", "Raging Fury", "Relic Song", "Revival Blessing", "Ruination",
               "Salt Cure", "Secret Sword", "Shed Tail", "Shell Trap", "Silk Trap", "Sketch", "Snap Trap", "Snarl",
               "Snatch", "Snore", "Snowscape", "Spectral Tief", "Spicy Extract", "Spiky Shield", "Spirit Break",
               "Spotlight", "Steam Eruption", "Steel Beam", "Strange Steam", "Struggle", "Sunsteel Strike",
               "Surging Strikes", "Switcheroo", "Techno Blast", "Thief", "Thousand Arrows", "Thousand Waves",
               "Thunder Cage", "Thunderous Kick", "Tidy Up", "Trailblaze", "Transform", "Trick", "Twin Beam",
               "V-create", "Wicked Blow", "Wicked Torque", "Wide Guard"]

OHKO = ["Fissure", "Guillotine", "Horn Drill", "Sheer Cold"]
NEVER = ["False Swipe", "Natures Madness", "Ruination", "Endeavor", "Super Fang"]
AutoCrit = ["Flower Trick", "Frost Breath", "Storm Throw", "Surging Strikes", "Wicked Blow", "Zippy Zap"]

TypeList = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground",
            "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

normal = dict(normal=1, fire=1, water=1, grass=1, bug=1, ice=1, electric=1, flying=1, ground=1, rock=.5, steel=.5,
              fairy=1, dragon=1, psychic=1, dark=1, ghost=0, fighting=1, poison=1)
fire = dict(normal=1, fire=1, water=.5, grass=2, bug=2, ice=2, electric=1, flying=1, ground=1, rock=.5, steel=2,
            fairy=1, dragon=.5, psychic=1, dark=1, ghost=1, fighting=1, poison=1)
water = dict(normal=1, fire=2, water=.5, grass=.5, bug=1, ice=1, electric=1, flying=1, ground=2, rock=2, steel=1,
             fairy=1, dragon=.5, psychic=1, dark=1, ghost=1, fighting=1, poison=1)
grass = dict(normal=1, fire=.5, water=2, grass=.5, bug=.5, ice=1, electric=1, flying=.5, ground=2, rock=2, steel=.5,
             fairy=1, dragon=.5, psychic=1, dark=1, ghost=1, fighting=1, poison=5.)
bug = dict(normal=1, fire=.5, water=1, grass=2, bug=.5, ice=1, electric=1, flying=.5, ground=1, rock=.1, steel=.5,
           fairy=.5, dragon=1, psychic=2, dark=2, ghost=.5, fighting=.5, poison=.5)
ice = dict(normal=1, fire=.5, water=.5, grass=2, bug=1, ice=.5, electric=1, flying=2, ground=2, rock=1, steel=.5,
           fairy=1, dragon=2, psychic=1, dark=1, ghost=1, fighting=1, poison=1)
electric = dict(normal=1, fire=1, water=2, grass=.5, bug=1, ice=1, electric=.5, flying=2, ground=0, rock=1, steel=1,
                fairy=1, dragon=.5, psychic=1, dark=1, ghost=1, fighting=1, poison=1)
flying = dict(normal=1, fire=1, water=1, grass=2, bug=2, ice=1, electric=.5, flying=1, ground=1, rock=.5, steel=.5,
              fairy=1, dragon=1, psychic=1, dark=1, ghost=1, fighting=2, poison=1)
ground = dict(normal=1, fire=2, water=1, grass=.5, bug=.5, ice=1, electric=2, flying=0, ground=1, rock=2, steel=2,
              fairy=1, dragon=1, psychic=1, dark=1, ghost=1, fighting=1, poison=2)
rock = dict(normal=1, fire=2, water=1, grass=1, bug=2, ice=2, electric=1, flying=2, ground=.5, rock=1, steel=.5,
            fairy=1, dragon=1, psychic=1, dark=1, ghost=1, fighting=.5, poison=1)
steel = dict(normal=1, fire=.5, water=.5, grass=1, bug=1, ice=2, electric=.5, flying=1, ground=1, rock=2, steel=.5,
             fairy=2, dragon=1, psychic=1, dark=1, ghost=1, fighting=1, poison=1)
fairy = dict(normal=1, fire=.5, water=1, grass=1, bug=1, ice=1, electric=1, flying=1, ground=1, rock=1, steel=.5,
             fairy=1, dragon=2, psychic=1, dark=2, ghost=1, fighting=2, poison=.5)
dragon = dict(normal=1, fire=1, water=1, grass=1, bug=1, ice=1, electric=1, flying=1, ground=1, rock=1, steel=.5,
              fairy=0, dragon=2, psychic=1, dark=1, ghost=1, fighting=1, poison=1)
psychic = dict(normal=1, fire=1, water=1, grass=1, bug=1, ice=1, electric=1, flying=1, ground=1, rock=1, steel=.5,
               fairy=1, dragon=1, psychic=.5, dark=0, ghost=1, fighting=2, poison=2)
ghost = dict(normal=0, fire=1, water=1, grass=1, bug=1, ice=1, electric=1, flying=1, ground=1, rock=1, steel=1, fairy=1,
             dragon=1, psychic=2, dark=.5, ghost=2, fighting=1, poison=1)
dark = dict(normal=1, fire=1, water=1, grass=1, bug=1, ice=1, electric=1, flying=1, ground=1, rock=1, steel=1, fairy=.5,
            dragon=1, psychic=2, dark=.5, ghost=2, fighting=.5, poison=1)
fighting = dict(normal=2, fire=1, water=1, grass=1, bug=.5, ice=2, electric=1, flying=.5, ground=1, rock=2, steel=2,
                fairy=.5, dragon=1, psychic=.5, dark=2, ghost=0, fighting=1, poison=.5)
poison = dict(normal=1, fire=1, water=1, grass=2, bug=1, ice=1, electric=1, flying=1, ground=.5, rock=.5, steel=0,
              fairy=2, dragon=1, psychic=1, dark=1, ghost=.5, fighting=1, poison=.5)

typeMatchups = dict(Normal=normal, Fire=fire, Water=water, Grass=grass, Bug=bug, Ice=ice, Electric=electric,
                    Flying=flying, Ground=ground, Rock=rock, Steel=steel, Fairy=fairy, Dragon=dragon, Psychic=psychic,
                    Ghost=ghost, Dark=dark, Fighting=fighting, Poison=poison)


def physicalMoveCalc(Move):
    pass


def fillBannedMoves():
    pass


def readMoves():
    pass


def calculateDamageModifier(moveType, types):
    pass


def getTypeMatchups(pokemon):
    Quarter = []
    Half = []
    Neutral = []
    Double = []
    Quad = []
    Immune = []
    Error = []
    Modifier = 1

    for entry in TypeList:
        for types in pokemon.types:
            Modifier = Modifier * typeMatchups.get(entry).get(types)
        if Modifier == .25:
            Quarter.append(entry)
        elif Modifier == .5:
            Half.append(entry)
        elif Modifier == 1.0:
            Neutral.append(entry)
        elif Modifier == 2.0:
            Double.append(entry)
        elif Modifier == 4.0:
            Quad.append(entry)
        elif Modifier == 0:
            Immune.append(entry)
        else:
            Error.append((entry, Modifier))
        Modifier = 1

    # print("Immune:", Immune)
    # print("Quarter:", Quarter)
    # print("Half:", Half)
    # print("Neutral:", Neutral)
    # print("Double:", Double)
    # print("Quad:", Quad)
    # print("Error:", Error)

    return Immune, Quarter, Half, Neutral, Double, Quad, Error


userIN = input("pokemon name: ")
pokemon = pypokedex.get(name=userIN)
# print(pokemon.name, pokemon.types)
a,b,c,d,e,f,g = getTypeMatchups(pokemon)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
