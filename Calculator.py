import csv
import math
import pypokedex


class Move:
    def __init__(self, name, moveType, moveCat, power, accuracy):
        self.name = name
        self.moveType = moveType
        self.category = moveCat
        self.power = int(power)
        self.accuracy = int(accuracy)


class Pokemon:
    def __init__(self, name, level, hpEV, atkEV, defEV, spaEV, spdEV, speEV, nature, currentHP, ability):

        # Nature Things
        atkMod = 1
        defMod = 1
        spaMod = 1
        spdMod = 1
        speMod = 1

        NoChange = ["hardy", "docile", "bashful", "quirky", "serious"]
        atkUp = ["lonely", "adamant", "naughty", "brave"]
        atkDw = ["bold", "modest", "calm", "timid"]
        defUp = ["bold", "impish", "lax", "relaxed"]
        defDw = ["lonely", "mild", "gentle", "hasty"]
        spaUp = ["modest", "mild", "rash", "quiet"]
        spaDw = ["adamant", "impish", "careful", "jolly"]
        spdUp = ["calm", "gentle", "careful", "sassy"]
        spdDw = ["naughty", "lax", "rash", "naive"]
        speUp = ["timid", "hasty", "jolly", "naive"]
        speDw = ["brave", "relaxed", "quiet", "sassy"]

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

        # End Nature Things

        self.name = name
        self.level = level
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
        self.pkmn = pypokedex.get(name=self.name)
        self.types = self.pkmn.types

        self.quarter, self.half, self.neutral, self.double, self.quad, self.immune, self.error = getTypeMatchups(
            self.pkmn)
        self.ability = ability
        self.status = "healthy"

        # Figure Out Stats (Pre Stat Buffs/Nerfs)
        self.HP = math.floor((((2 * self.pkmn.base_stats.hp + self.hpI + (
            math.floor(self.hpE / 4))) * self.level) / 100) + self.level + 10)
        self.ATK = math.floor(((((2 * self.pkmn.base_stats.attack + self.atkI + (
            math.floor(self.atkE / 4))) * self.level) / 100) + 5) * atkMod)
        self.DEF = math.floor(((((2 * self.pkmn.base_stats.defense + self.defI + (
            math.floor(self.defE / 4))) * self.level) / 100) + 5) * defMod)
        self.SPA = math.floor(((((2 * self.pkmn.base_stats.sp_atk + self.spaI + (
            math.floor(self.spaE / 4))) * self.level) / 100) + 5) * spaMod)
        self.SPD = math.floor(((((2 * self.pkmn.base_stats.sp_def + self.spdI + (
            math.floor(self.spdE / 4))) * self.level) / 100) + 5) * spdMod)
        self.SPE = math.floor(((((2 * self.pkmn.base_stats.speed + self.speI + (
            math.floor(self.speE / 4))) * self.level) / 100) + 5) * speMod)


Testing = True
testPokemonName = "Clefable"
testHpA = 252
testAtkA = 0
testDefA = 200
testSpaA = 56
testSpdA = 0
testSpeA = 0
testCurrHpA = 394
testNatureA = "modest"
testAbilityA = "magic guard"

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

OHKO = ["fissure", "guillotine", "horn drill", "sheer cold"]
NEVER = ["false swipe", "natures madness", "ruination", "endeavor", "super fang"]
AutoCrit = ["flower trick", "frost breath", "storm throw", "surging strikes", "wicked blow", "zippy zap"]
NatureList = ["hardy", "lonely", "brave", "adamant", "naughty", "bold", "docile", "relaxed", "impish", "lax", "timid",
              "hasty", "serious", "jolly", "naive", "modest", "mild", "quiet", "bashful", "rash", "calm", "sassy",
              "gentle", "careful", "quirky"]
Bulletproof = ["acid spray", "aura sphere", "barrage", "beak blast", "bullet seed", "egg bomb", "electro ball",
               "energy ball", "focus blast", "gyro ball", "ice ball", "magnet bomb", "mist ball", "mud bomb",
               "octazooka", "pollen puff", "pyro ball", "rock blast", "rock wrecker", "searing shot", "seed bomb",
               "shadow ball", "sludge bomb", "weather bomb", "zap cannon"]
Soundproof = ["boomburst", "bug buzz", "chatter", "clanging scales", "clangorous soul", "clangorous soulblaze",
              "confide", "disarming voice", "echoed voice", "eerie spell", "grass whistle", "growl", "heal bell",
              "howl", "hyper voice", "metal sound", "noble roar", "overdrive", "parting shot", "perish song",
              "relic song", "roar", "screech", "shadow panic", "sing", "snarl", "snore", "sparkling aria", "supersonic",
              "torch song", "uproar"]
MultiHit = ["arm thrust", "barrage", "bone rush", "bullet seed", "comet punch", "double slap", "fury attack",
            "fury swipes", "icicle spear", "pin missile", "rock blast", "scale shot", "spike cannon", "tail slap",
            "water shuriken"]
FixedMulti = ["bonemerang", "double hit", "double iron bash", "double kick", "dragon darts", "dual chop",
              "dual wingbeat", "gear grind", "surging strikes", "triple dive", "twin beam", "twin needle"]
AccuracyMulti = ["triple axel", "triple kick", "population bomb"]
Damp = ["explosion", "self-destruct", "mind blown", "misty explosion"]
TypeImmune = dict(levitate="ground", voltabsorb="electric", waterabsorb="water", lightningrod="electric",
                  stormdrain="water", eartheater="ground", flashfire="fire", motordrive="electric",
                  dryskin="water", sapsipper="grass")
IgnoreAbilities = ["mold breaker", "mycelium might", "teravolt", "turboblaze"]
TypeList = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground",
            "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
MoveList = []

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


def removeBannedMoves():
    for entries in MoveList:
        if entries.name in bannedMoves:
            MoveList.remove(entries)


def readMoves(path):
    times = 0
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if times == 0:
                times = 1
            else:
                MoveList.append(Move(row[0].lower(), row[1].lower(), row[2].lower(), row[3], row[4]))


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

    return Quarter, Half, Neutral, Double, Quad, Immune, Error


def getDamageRolls(user, move, target, currentWeather, glaive):
    DamageRolls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # print(move.moveType)
    if move.moveType in user.quarter:
        TypeMatchup = .25
    elif move.moveType in user.half:
        TypeMatchup = .5
    elif move.moveType in user.double:
        TypeMatchup = 2
    elif move.moveType in user.quad:
        TypeMatchup = 4
    elif move.moveType in user.immune:
        TypeMatchup = 0
    else:
        TypeMatchup = 1

    if target.ability in TypeImmune:
        if TypeImmune.get(target.ability).lower() == move.moveType and user.ability not in IgnoreAbilities:
            TypeMatchup = 0
            print("immune through ability")

    if move.name in OHKO:
        for x in range(16):
            DamageRolls[x] = 9999
        return DamageRolls

    if move.category.lower() == "physical":
        offense = user.ATK
        defense = target.DEF
        #print(move.name, "ATK", user.ATK, target.DEF)
    elif move.category.lower() == "special":
        offense = user.SPA
        if move.name.lower() == "psyshock":
            defense = target.DEF
            #print(move.name, "SPATK", user.SPA, target.DEF)
        else:
            defense = target.SPD
            #print(move.name, "SPATK", user.SPA, target.SPD)
    elif move.category.lower() == "status":
        for x in range(16):
            DamageRolls[x] = 0
        return DamageRolls

    # Actual Damage being Calculated
    for random in range(85, 101):
        part1 = ((2 * user.level / 5) + 2)
        part2 = (move.power * float(offense / defense))
        mainMultiplier = (part1 * part2 / 50) +2

        Other = 1  # Technically means nothing for now
        Targets = 1
        PB = 1  # This will be used for Parental Bond SOON(ish)

        # Burn Calculation
        if user.status.lower() == "burn" and move.category.lower() == "physical" and user.ability.lower() != "guts":
            Burn = .5
        else:
            Burn = 1

        # Weather Factors
        if user.ability == "cloud nine" or user.ability == "air lock" or target.ability == "cloud nine" or target.ability == "air lock":
            Weather = 1
        elif currentWeather.lower() == "rain":
            if move.moveType.lower() == "water":
                Weather = 1.5
            elif move.moveType.lower() == "fire":
                Weather = .5
        elif currentWeather.lower() == "sun":
            if move.name.lower() == "hydro steam" or move.moveType.lower() == "fire":
                Weather = 1.5
            elif move.moveType.lower() == "water":
                Weather = .5
        elif currentWeather.lower() == "sand" or currentWeather.lower() == "snow":
            if move.name.lower() == "solar beam" or move.name.lower() == "solar blade":
                Weather = .5
        else:
            Weather = 1
        if currentWeather == "snow" and "ice" in target.types:
            defense = defense * 1.5

        # Stab (Including Adaptability)
        if move.moveType not in user.types:
            STAB = 1
        elif user.ability.lower == "adaptability":
            STAB = 2
        else:
            STAB = 1.5

        Critical = 1  # Deal with Crits Later

        ThisRoll = math.floor(mainMultiplier * Targets * PB * Weather * glaive * Critical * float(random / 100) * STAB * TypeMatchup * Burn)
        if random == 100:
            print(move.name + ":", mainMultiplier, Targets,PB,Weather,glaive,Critical, float(random/100), STAB, TypeMatchup, Burn)
        DamageRolls[random - 85] = ThisRoll

    return DamageRolls


# Get Pokemon A
while True:
    if Testing:
        userIn = testPokemonName
        pkmnA = pypokedex.get(name="Clefable")
        break
    else:
        try:
            userIn = input("Enter a Pokemon: ").lower()
            pkmnA = pypokedex.get(name=userIn)
            break
        except:
            print("Something went wrong, try again ")

# Get Level A
while True:
    if Testing:
        pkmnAlvl = 100
        break
    else:
        try:
            pkmnAlvl = input("Please Enter the Pokemon's Level ")
            if int(pkmnAlvl) >= 1 and int(pkmnAlvl) <= 100:
                pkmnAlvl = int(pkmnAlvl)
                break
            else:
                print("Level fell outside of the allowed range ")
        except ValueError:
            print("Error")

# Get HP EVs A
while True:
    if Testing:
        pkmnAhp = testHpA
        break
    else:
        try:
            pkmnAhp = input("Please Enter the HP EVs ")
            if 0 <= int(pkmnAhp) <= 252:
                pkmnAhp = int(pkmnAhp)
                break
            else:
                print("EVs fell outside of the allowed range ")
        except ValueError:
            print("Error")

# Get Attack EVs A
while True:
    if Testing:
        pkmnAatk = testAtkA
        break
    else:
        try:
            pkmnAatk = input("Please Enter the Attack EVs ")
            if 0 <= int(pkmnAatk) <= 252:
                pkmnAatk = int(pkmnAatk)
                break
            else:
                print("EVs fell outside of the allowed range ")
        except ValueError:
            print("Error")

# Get Defense EVs A
while True:
    if Testing:
        pkmnAdef = testDefA
        break
    else:
        try:
            pkmnAdef = input("Please Enter the Defense EVs ")
            if 0 <= int(pkmnAdef) <= 252:
                pkmnAdef = int(pkmnAdef)
                break
            else:
                print("EVs fell outside of the allowed range ")
        except ValueError:
            print("Error")

# Get Special Attack EVs A
while True:
    if Testing:
        pkmnAspa = testSpaA
        break
    else:
        try:
            pkmnAspa = input("Please Enter the Special Attack EVs ")
            if 0 <= int(pkmnAspa) <= 252:
                pkmnAspa = int(pkmnAspa)
                break
            else:
                print("EVs fell outside of the allowed range ")
        except ValueError:
            print("Error")

# Get Special Defense EVs A
while True:
    if Testing:
        pkmnAspd = testSpdA
        break
    else:
        try:
            pkmnAspd = input("Please Enter the Special Defense EVs ")
            if 0 <= int(pkmnAspd) <= 252:
                pkmnAspd = int(pkmnAspd)
                break
            else:
                print("EVs fell outside of the allowed range ")
        except ValueError:
            print("Error")

# Get Speed EVs A
while True:
    if Testing:
        pkmnAspe = testSpeA
        break
    else:
        try:
            pkmnAspe = input("Please Enter the Speed EVs ")
            if 0 <= int(pkmnAspe) <= 252:
                pkmnAspe = int(pkmnAspe)
                break
            else:
                print("EVs fell outside of the allowed range ")
        except ValueError:
            print("Error")

# Get Current HP A
while True:
    if Testing:
        currHP = testCurrHpA
        break
    else:
        try:
            currHP = input("Please Enter the Current HP ")
            if 0 <= int(currHP) <= math.floor(
                    (((2 * int(pkmnA.base_stats.hp) + 31 + (math.floor(int(pkmnAhp) / 4))) * int(
                        pkmnAlvl)) / 100) + int(
                        pkmnAlvl) + 10):
                break
            else:
                print("HP fell outside of the allowed range ")
        except ValueError:
            print("Error")

# Get Nature A
while True:
    if Testing:
        pkmnAnat = testNatureA
        break
    else:
        pkmnAnat = input("Please Enter the Nature ").lower()
        if pkmnAnat in NatureList:
            break
        else:
            print("No such nature exists")

# Get Ability A
while True:
    if Testing:
        abilityA = testAbilityA
    else:
        abilityA = input("Please Enter the Ability ").lower()
    break

pokemonA = Pokemon(userIn, pkmnAlvl, pkmnAhp, pkmnAatk, pkmnAdef, pkmnAspa, pkmnAspd, pkmnAspe, pkmnAnat, currHP,
                   abilityA)

# Get Pokemon B
while True:
    try:
        userIn = input("Enter a Pokemon: ").lower()
        pkmnB = pypokedex.get(name=userIn)
        break
    except:
        print("Something went wrong, try again ")

# Get Level B
while True:
    try:
        pkmnBlvl = input("Please Enter the Pokemon's Level ")
        if int(pkmnBlvl) >= 1 and int(pkmnBlvl) <= 100:
            pkmnBlvl = int(pkmnBlvl)
            break
        else:
            print("Level fell outside of the allowed range ")
    except ValueError:
        print("Error")

# Get HP EVs B
while True:
    try:
        pkmnBhp = input("Please Enter the HP EVs ")
        if 0 <= int(pkmnBhp) <= 252:
            pkmnBhp = int(pkmnBhp)
            break
        else:
            print("EVs fell outside of the allowed range ")
    except ValueError:
        print("Error")

# Get Attack EVs B
while True:
    try:
        pkmnBatk = input("Please Enter the Attack EVs ")
        if 0 <= int(pkmnBatk) <= 252:
            pkmnBatk = int(pkmnBatk)
            break
        else:
            print("EVs fell outside of the allowed range ")
    except ValueError:
        print("Error")

# Get Defense EVs B
while True:
    try:
        pkmnBdef = input("Please Enter the Defense EVs ")
        if 0 <= int(pkmnBdef) <= 252:
            pkmnBdef = int(pkmnBdef)
            break
        else:
            print("EVs fell outside of the allowed range ")
    except ValueError:
        print("Error")

# Get Special Attack EVs B
while True:
    try:
        pkmnBspa = input("Please Enter the Special Attack EVs ")
        if 0 <= int(pkmnBspa) <= 252:
            pkmnBspa = int(pkmnBspa)
            break
        else:
            print("EVs fell outside of the allowed range ")
    except ValueError:
        print("Error")

# Get Special Defense EVs B
while True:
    try:
        pkmnBspd = input("Please Enter the Special Defense EVs ")
        if 0 <= int(pkmnBspd) <= 252:
            pkmnBspd = int(pkmnBspd)
            break
        else:
            print("EVs fell outside of the allowed range ")
    except ValueError:
        print("Error")

# Get Speed EVs B
while True:
    try:
        pkmnBspe = input("Please Enter the Speed EVs ")
        if 0 <= int(pkmnBspe) <= 252:
            pkmnBspe = int(pkmnBspe)
            break
        else:
            print("EVs fell outside of the allowed range ")
    except ValueError:
        print("Error")

# Get Current HP Percentage B
while True:
    try:
        currHPB = input("Please Enter the Current HP Percentage ")
        if 1 <= 100:
            break
        else:
            print("HP fell outside of the allowed range ")
    except ValueError:
        print("Error")

# Get Nature B
while True:
    pkmnBnat = input("Please Enter the Nature ").lower()
    if pkmnBnat in NatureList:
        break
    else:
        print("No such nature exists")

# Get Ability B
while True:
    abilityB = input("Please Enter the Ability ").lower()
    break

pokemonB = Pokemon(userIn, pkmnBlvl, pkmnBhp, pkmnBatk, pkmnBdef, pkmnBspa, pkmnBspd, pkmnBspe, pkmnBnat, currHPB,
                   abilityB)
# Finally Correct Current HP math
varA = pypokedex.get(name=userIn).base_stats.hp
varB = math.floor(pkmnBhp / 4)
varC = pkmnBlvl / 100
varD = pkmnBlvl + 10
pokemonB.currentHP = (((2 * varA) + 31 + varB) * varC) + varD

# print(pokemonB.name)
# print(pokemonB.HP)
# print(pokemonB.ATK)
# print(pokemonB.DEF)
# print(pokemonB.SPA)
# print(pokemonB.SPD)
# print(pokemonB.SPE)

readMoves("PokemonMoves.csv")
removeBannedMoves()

# for moves in MoveList:
#     if moves.power == -1 and moves.name not in OHKO:
#         print(moves.name, moves.moveType, moves.category, moves.power, moves.accuracy)

KillingRolls = 0
LosingRolls = 0

for moves in MoveList:
    Rolls = getDamageRolls(pokemonA, moves, pokemonB, "none", 1)
    print(moves.name, Rolls[15])
    for roll in Rolls:
        if roll >= pokemonB.currentHP:
            KillingRolls = KillingRolls + 1
            # print(moves.name)
        else:
            LosingRolls = LosingRolls + 1

print("winning rolls", KillingRolls)
print("losing rolls", LosingRolls)
print(pokemonB.types)
print(pokemonA.types)
print(pokemonB.pkmn.types[0])
print(pokemonA.pkmn.types[0])

moonblast = Move("moonblast", "fairy", "special", 95, 100)
#Rolls = getDamageRolls(pokemonA, moonblast, pokemonB, "none", 1)
#print(Rolls)
# for roll in Rolls:
#     if roll >= pokemonB.currentHP:
#
#         print("Win", roll)
#     else:
#         print("Loss", roll)
