import csv
import math
import pypokedex
from pypokedex.exceptions import *



class Move:
    def __init__(self, name, moveType, power, accuracy):
        self.name = name
        self.moveType = moveType
        self.power = power
        self.accuracy = accuracy


class Pokemon:
    def __init__(self, name, hpEV, atkEV, defEV, spaEV, spdEV, speEV, nature, currentHP):

        #Nature Things
        atkMod = 1
        defMod = 1
        spaMod = 1
        spdMod = 1
        speMod = 1

        NoChange = ["hardy", "docile", "bashful", "quirky", "serious"]
        atkUp = ["lonely","adamant","naughty","brave"]
        atkDw = ["bold","modest","calm","timid"]
        defUp = ["bold","impish","lax","relaxed"]
        defDw = ["lonely","mild","gentle","hasty"]
        spaUp = ["modest","mild","rash","quiet"]
        spaDw = ["adamant","impish","careful","jolly"]
        spdUp = ["calm","gentle","careful","sassy"]
        spdDw = ["naughty","lax","rash","naive"]
        speUp = ["timid","hasty","jolly","naive"]
        speDw = ["brave","relaxed","quiet","sassy"]

        if nature in atkUp:
            atkMod = 1.1
        elif nature in atkDw:
            atkMod = 0.9
        else:
            atkMod = 1

        if nature in defUp:
            defMod = 1.1
        elif nature in defDw:
            defMod = 0.9
        else:
            defMod = 1

        if nature in spaUp:
            spaMod = 1.1
        elif nature in spaDw:
            spaMod = 0.9
        else:
            spaMod = 1

        if nature in spdUp:
            spdMod = 1.1
        elif nature in spdDw:
            spdMod = 0.9
        else:
            spdMod = 1

        if nature in speUp:
            speMod = 1.1
        elif nature in speDw:
            speMod = 0.9
        else:
            speMod = 1

    #End Nature Things

        self.name = name
        self.level = 100
        self.currentHP = currentHP
        self.hpE = hpEV
        self.hpI = 31
        self.atkE = atkEV
        self.atkI = 31
        self.defE = defEV
        self.defI = 31
        self.spaE = spaEV
        self.spaI = 31
        self.spdE = spdEV
        self.spdI = 31
        self.speE = speEV
        self.speI = 31
        self.pokemon = pypokedex.get(name=self.name)
        self.types = pokemon.types
        self.quarter, self.half, self.neutral, self.double, self.quad, self.immune, self.error = getTypeMatchups(pokemon)

        #Figure Out Stats (Pre Stat Buffs/Nerfs)
        self.HP = math.floor((((2 * pokemon.base_stats.hp + self.hpI + (math.floor(self.hpE / 4))) * self.level) / 100) + self.level + 10)
        self.ATK = math.floor(((((2 * pokemon.base_stats.attack + self.atkI + (math.floor(self.atkE / 4))) * self.level) / 100) + 5) * atkMod)
        self.DEF = math.floor(((((2 * pokemon.base_stats.defense + self.defI + (math.floor(self.defE / 4))) * self.level) / 100) + 5) * defMod)
        self.SPA = math.floor(((((2 * pokemon.base_stats.sp_atk + self.spaI + (math.floor(self.spaE / 4))) * self.level) / 100) + 5) * spaMod)
        self.SPD = math.floor(((((2 * pokemon.base_stats.sp_def + self.spdI + (math.floor(self.spdE / 4))) * self.level) / 100) + 5) * spdMod)
        self.SPE = math.floor(((((2 * pokemon.base_stats.speed + self.speI + (math.floor(self.speE / 4))) * self.level) / 100) + 5) * speMod)


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

    return Quarter, Half, Neutral, Double, Quad, Immune, Error


while True:
    try:
        userIn = input("Enter a Pokemon: ").lower()
        pokemon = pypokedex.get(name=userIn)
        break
    except PyPokedexHTTPError:
        print("Something went wrong, try again")
