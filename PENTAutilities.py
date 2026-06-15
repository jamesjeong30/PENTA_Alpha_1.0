import time
import os
import random
import sys
import copy
import string
import math
from PENTAmusic import AudioManager



# What we are going to save in the JSON file
character = {
    # Settings
    "Volume": 55,
    "Astral Convergence Long-String": True,
    "New Battle": False,


    # Stats
    "Name": "Player",
    "POTENTIAL": 0,
    "Sponsor": None,
    "Held_Weapon": None,
    "Held_Armor": None,
    "Strength": 100,
    "Defense": 10,
    "Health": 100,
    "Mana": 500,
    "Mana Regen": 25,
    "Wisdom": 0,
    "Luck": 0,
    "Dodge": 1,
    "Parry": 1,
    "Critical": 1,
    "Stat Inheritance": 0.01,
    "Skill": "???",

    # Sefirot Affinities
    "Eloki": 1,"Keter": 1, "Chokmah": 1, "Binah": 1,
    "Chesed": 1, "Gevurah": 1, "Tiferet": 1,
    "Netzach": 1, "Hod": 1, "Yesod": 1, "Malkhut": 1,


    # Buffs
    "Buffs": {},

    # Items
    "Inventory": ["'Moss' {Common}", "'Stick' {Common}", "'Iron' {Uncommon}"],

    # Progression
    "Location": None,
    "Coordinates": None,
    "Been There": [[-967, 10]],

    # Miscellaneous I
    "Shrines": {"armageddon_shrine": False},

    "Chest": {"Chest_1": False},
    "Barrel": {"Barrel_1": False},
    "Corpse": {"Corpse_1": False},
    "Cache": {"Cache_1": False},
    
    "Lore": {"Lore_1": False, "Lore_2": False},

    # Miscellaneous II
    "End_of_Zone": {"sfz1": False},
    "Hidden_Bosses": {"The Builder": False},
    "Sponsor_Offer": {"The Farmer": False},

    # Emperors & Gods
    "Emperors": {"Fourth": {"Death": False, "Encounter": False}},
    "Gods": {}
                }




buffs = {
    "Weapon Up": {"Strength": 100, "Cost": 10, "Duration": 2},
    "Stone Skin": {"Defense": 50, "Cost": 50, "Duration": 3},
    "Pierce": {"Strength": 50, "Cost": 30, "Duration": 3},
    "Fortify": {"Defense": 100, "Cost": 200, "Duration": 5},
    "Halo": {"Strength": 150, "Mana": 250, "Cost": 100, "Duration": 4},
    "Quick Movements": {"All_Multiply": True, "Dodge": 2, "Cost": 200, "Duration": 3},
    "Light Speed": {"All_Multiply": True, "Dodge": 2, "Parry": 2, "Cost": 300, "Duration": 2},
    "Light Barrier": {"Defense": 250, "Cost": 250, "Duration": 4},
    "Last Stand": {"Add_Multiply": True, "Defense": 100, "Defense_Multiplier": 2, "Cost": 500, "Duration": 1},
    "Overclock": {"All_Multiply": True, "Strength": 2, "Cost": 500, "Duration": 2},
    "Overload": {"All_Multiply": True, "Mana": 2, "Cost": 500, "Duration": 2},
    "King of the Hill": {"Add_Multiply": True, "Defense": 500, "Defense_Multiplier": 1.25, "Cost": 1000, "Duration": 1},
    "Perfect Form": {"Strength": 1250, "Defense": 1250, "Health": 1250, "Mana": 1250, "Cost": 1250, "Duration": 3},
    "Miracle": {"Defense": 10000, "Cost": 1, "Duration": 1},
    "Holy Shield": {"All_Multiply": True, "Defense": 3, "Cost": 1500, "Duration": 2},
    "Holy Halo": {"All_Multiply": True, "Health": 2, "Cost": 1300, "Duration": 3},
    "Mana Halo": {"All_Multiply": True, "Mana": 3, "Cost": 2000, "Duration": 2},
    "Indestructible": {"All_Multiply": True, "Health": 2, "Defense": 3, "Cost": 2500, "Duration": 3},
    "Mana Shield": {"Custom": True, "Defense": 500, "Cost": "Half of Mana", "Duration": 1},
    "Rhythm": {"Custom": True, "Cost": 0, "Duration": 3},
    "Divine Rhythm": {"Custom": True, "Cost": 0, "Duration": 3},
    "Flash Insight": {"Random": True, "Wisdom": 2500, "Cost": 3000, "Duration": 3},
    "Primordial Sight": {"All_Multiply": True, "Critical": 55, "Cost": 5000, "Duration": 3},
    "Divine Overclock": {"All_Multiply": True, "Strength": 5.5, "Cost": 5000, "Duration": 3},
    "Divine Overdrive": {"All_Multiply": True, "Mana": 5.5, "Cost": 5000, "Duration": 3},
    "Infinite Insight": {"Random": True, "Wisdom": 5000, "Cost": 5000, "Duration": 3},
    "Divine Focus": {"Random": True, "Critical": 20, "Dodge": 20, "Luck": 30, "Cost": 1, "Duration": 3},
    "Absolute Focus": {"Random": True, "Critical": 25, "Dodge": 25, "Luck": 10, "Cost": 1, "Duration": 3},
    "Structation": {"Random": True, "Defense": 5555, "Cost": 2000, "Duration": 3},
    "The Seventh Light": {"Random": True, "Strength": 3355, "Defense": 3555, "Mana": 3335, "Health": 3333,
                          "Wisdom": 5333, "Luck": 10, "Dodge": 10, "Parry": 10, "Critical": 10, "Cost": 5555, "Duration": 2},
    "Perfect Defense": {"Add_Multiply": True, "Defense": 10000, "Defense_Multiplier": 3.5, "Cost": 5000, "Duration": 1},
    "Will of the Crown": {"Add_Multiply": True, "Strength": 10000, "Defense": 10000, "Health": 10000, "Mana": 10000,
                          "Strength_Multiplier": 5, "Defense_Multiplier": 5, "Health_Multiplier": 5, "Mana_Multiplier": 5,
                          "Cost": 25000, "Duration": 1}
    }

debuffs = {}

# Can make it so that it adds a percentage of the character's stats instead of multiply it
def apply_buff(battle_character, buff_name):
    global character
    buff = buffs[buff_name]
    if buff.get("Add_Multiply") == True:
        for stat, value in buff.items():
            if stat == "Strength" or stat == "Defense" or stat == "Health" or stat == "Mana":
                battle_character[stat] += value
                if battle_character["Buffs"].get(buff_name) == None:
                    battle_character["Buffs"].update({buff_name: {stat: value}})
                else:
                    battle_character["Buffs"][buff_name].update({stat: value})

        for stat, value in buff.items():
            if stat == "Defense_Multiplier" or stat == "Strength_Multiplier" or stat == "Health_Multiplier" or stat == "Mana_Multiplier":
                stat = stat.split("_")[0].strip()
                battle_character[stat] += (value - 1)*battle_character[stat]
                if battle_character["Buffs"].get(buff_name) == None:
                    battle_character["Buffs"][buff_name].update({stat.split("_")[0].strip(): (value - 1)*battle_character[stat]})
                else:
                    battle_character["Buffs"][buff_name][stat.split("_")[0].strip()] += (value - 1)*battle_character[stat]

        battle_character["Buffs"][buff_name].update({"Cost": buff["Cost"]})
        battle_character["Buffs"][buff_name].update({"Duration": buff["Duration"] + 1})
        return battle_character
        


    elif buff.get("All_Multiply") == True:
        temp_list_b = ["Duration", "Cost", "All_Multiply"]
        for stat, value in buff.items():
            if stat not in temp_list_b:
                battle_character[stat] += (value - 1)*battle_character[stat]
                if battle_character["Buffs"].get(buff_name) == None:
                    battle_character["Buffs"].update({buff_name: {stat: (value - 1)*battle_character[stat]}})
        battle_character["Buffs"][buff_name].update({"Cost": buff["Cost"]})
        battle_character["Buffs"][buff_name].update({"Duration": buff["Duration"] + 1})
        return battle_character



    elif buff.get("Custom") == True:
        if buff_name == "Mana Shield":
            defense_value = battle_character["Mana"] / 2
            battle_character["Buffs"].update({buff_name: {"Cost": battle_character["Mana"] / 2}})
            battle_character["Buffs"][buff_name].update({"Defense": defense_value})
            battle_character["Mana"] -= defense_value
            battle_character["Defense"] += defense_value
            battle_character[battle_character["Buffs"][buff_name]["Defense"]] += 4*battle_character["Defense"]
            battle_character["Defense"] += 4*battle_character["Defense"]
            battle_character["Buffs"][buff_name].update({"Duration": buff["Duration"] + 1})
            return battle_character    

        elif buff_name == "Rhythm":
            battle_character["Buffs"].update({buff_name: {"Cost": buff["Cost"]}})
            battle_character["Buffs"][buff_name].update({"Duration": buff["Duration"] + 1})
            strength_value = (battle_character["Strength"] * 0.5 + math.sqrt((battle_character["Mana"]**2) - 2 * battle_character["Defense"] * battle_character["Health"] + 100000)) / (2 * (battle_character["Luck"] / 100))
            strength_value = round(strength_value, 2)
            battle_character["Buffs"][buff_name].update({"Strength": strength_value})
            battle_character["Strength"] += strength_value
            return battle_character

        elif buff_name == "Divine Rhythm":
            battle_character["Buffs"].update({buff_name: {"Cost": buff["Cost"]}})
            battle_character["Buffs"][buff_name].update({"Duration": buff["Duration"] + 1})
            strength_value = (battle_character["Strength"] * 1.59 + math.sqrt((battle_character["Mana"]**2) - 1.25 * battle_character["Defense"] * battle_character["Health"] + 100000)) / (1.25 * (battle_character["Luck"] / 120))
            strength_value = round(strength_value, 2)
            battle_character["Buffs"][buff_name].update({"Strength": strength_value})
            battle_character["Strength"] += strength_value
            return battle_character


    elif buff.get("Random") == True:
        temp_list_d = ["Duration", "Cost"]
        for stat, value in buff.items():
            if stat not in temp_list_d:
                random_number = random.random() * 5.5
                battle_character[stat] += round(random_number * value)
                if battle_character["Buffs"].get(buff_name) is None:
                    battle_character["Buffs"].update({buff_name: {stat: round(random_number * value)}})
                else:
                    battle_character["Buffs"][buff_name].update({stat: round(random_number * value)})
        
        battle_character["Buffs"][buff_name].update({"Cost": buff["Cost"]})
        battle_character["Buffs"][buff_name].update({"Duration": buff["Duration"] + 1})
        return battle_character


    else:
        temp_list_c = ["Duration", "Cost"]
        for stat, value in buff.items():
            if stat not in temp_list_c:
                battle_character[stat] += value
                if battle_character["Buffs"].get(buff_name) is None:
                    battle_character["Buffs"].update({buff_name: {stat: value}})
                else:
                    battle_character["Buffs"][buff_name].update({stat: value})
        
        battle_character["Buffs"][buff_name].update({"Cost": buff["Cost"]})
        battle_character["Buffs"][buff_name].update({"Duration": buff["Duration"] + 1})
        return battle_character



def tick_buffs(battle_character):
    global character
    expired = []

    for buff in list(battle_character["Buffs"].keys()):
        if battle_character["Buffs"][buff]["Duration"] == "Infinite":
            pass
        else:
            battle_character["Buffs"][buff]["Duration"] -= 1
            if battle_character['Buffs'][buff]['Duration'] <= 0:
                expired.append(buff)

    for buff_name in expired:
        battle_character = remove_buff(battle_character, buff_name)

    return battle_character

def remove_buff(battle_character, buff_name):
    global character
    temp_stat_list = ["Duration", "Cost"]
    for stat, value in battle_character["Buffs"][buff_name].items():
        if stat not in temp_stat_list:
            battle_character[stat] -= value

    battle_character["Mana"] += battle_character["Buffs"][buff_name]["Cost"]

    x = random.choice([f"The buff [{buff_name}] has expired.", 
                        f"The effects of [{buff_name}] has worn off.",
                        f"You feel your stats weakening as the buff [{buff_name}] expires.",
                        f"The buff [{buff_name}] has worn off, returning your stats to normal."])
    encounter_text(x)
    x = random.choice([f"You regain {buffs[buff_name]['Cost']} Mana through the expiration of the buff [{buff_name}].",
                        f"The expiration of the buff [{buff_name}] restores {buffs[buff_name]['Cost']} Mana.",
                        f"You feel a surge of Mana as the buff [{buff_name}] expires, restoring {buffs[buff_name]['Cost']} Mana."])
    encounter_text(x)
    del battle_character["Buffs"][buff_name]
    return battle_character



# How the stats look like during a battle
def b_character_create():
    battle_character = copy.deepcopy(character)
    return battle_character



# Enemy and Boss Data
enemies = {"Training Dummy": {"Name": "Training Dummy", "Affinity": "None", "Health": 1000000000, "Strength": 100, "Mana": 100, "Defense": 0},
           "Mossling": {"Name": "Mossling", "Affinity": "Malkhut", "Health": 150, "Strength": 50, "Mana": 50, "Defense": 0},
           "Pebblekin": {"Name": "Pebblekin", "Affinity": "Malkhut", "Health": 300, "Strength": 40, "Mana": 50, "Defense": 0},
           "Shadowkin": {"Name": "Shadowkin", "Affinity": "Malkhut", "Health": 250, "Strength": 60, "Mana": 100, "Defense": 0},
           "Forest Wisp": {"Name": "Forest Wisp", "Affinity": "Malkhut", "Health": 200, "Strength": 60, "Mana": 150, "Defense": 0},
           "Doofakle": {"Name": "Doofakle", "Affinity": "Yesod", "Health": 250, "Strength": 100, "Mana": 100, "Defense": 0},
           "Rock Golem": {"Name": "Rock Golem", "Affinity": "Yesod", "Health": 400, "Strength": 30, "Mana": 20, "Defense": 500},
           "Stigless": {"Name": "Stigless", "Affinity": "Yesod", "Health": 350, "Strength": 20, "Mana": 50, "Defense": 10},
           "Troph": {"Name": "Troph", "Affinity": "Netzach", "Health": 500, "Strength": 60, "Mana": 200, "Defense": 150},
           "Packer": {"Name": "Packer", "Affinity": "Netzach", "Health": 450, "Strength": 55, "Mana": 150, "Defense": 100},
           "Krossad": {"Name": "Krossad", "Affinity": "Malkhut", "Health": 300, "Strength": 60, "Mana": 50, "Defense": 0},
           "Quickling": {"Name": "Quickling", "Affinity": "Netzach", "Health": 200, "Strength": 20, "Mana": 100, "Defense": 0},
           "Giant Snake": {"Name": "Giant Snake", "Affinity": "Malkhut", "Health": 350, "Strength": 40, "Mana": 50, "Defense": 0},
           "Little Prince of the Forest": {"Name": "Little Prince of the Forest", "Affinity": "Yesod", "Health": 300, "Strength": 30, "Mana": 150, "Defense": 0},
           "One-eyed Birb": {"Name": "One-eyed Birb", "Affinity": "Netzach", "Health": 250, "Strength": 25, "Mana": 100, "Defense": 0},
           "Diddler": {},
           "Embark": {},
           "Ionic": {},
           "Kamacho": {}}

enemy_moves = {"Training Dummy": {"Stand": {"Damage": 0, "Cost": 0}},
               "Mossling": {"Swipe": {"Damage": enemies["Mossling"]["Strength"], "Cost": 5}, "Vines": {"Damage": enemies["Mossling"]["Mana"], "Cost": 5}},
               "Pebblekin": {"Rock Throw": {"Damage": enemies["Pebblekin"]["Strength"], "Cost": 5}, "Stone Slam": {"Damage": enemies["Pebblekin"]["Strength"], "Cost": 10}},
               "Forest Wisp": {"Spirit Bolt": {"Damage": enemies["Forest Wisp"]["Mana"] / 7, "Cost": 5}, "Forest Mist": {"Damage": enemies["Forest Wisp"]["Strength"] + enemies["Forest Wisp"]["Mana"] / 7, "Cost": 10}},
               "Doofakle": {"Doofa Slam": {"Damage": enemies["Doofakle"]["Strength"], "Cost": 10}, "Doofa Blast": {"Damage": enemies["Doofakle"]["Mana"], "Cost": 15}},
               "Rock Golem": {"Rock Throw": {"Damage": enemies["Rock Golem"]["Strength"], "Cost": 5}, "Stone Slam": {"Damage": enemies["Rock Golem"]["Defense"] * 3, "Cost": 10}}}

mini_bosses = {"The Giant Enemy Spider": {"Name": "The Giant Enemy Spider", "Affinity": "Malkhut", "Health": 500, "Strength": 75, "Mana": 300, "Defense": 100},
               "Night Hawk": {"Name": "Night Hawk", "Affinity": "Netzach", "Health": 450, "Strength": 70, "Mana": 250, "Defense": 80},
                 "Wickstrosity": {"Name": "Wickstrosity", "Affinity": "Yesod", "Health": 600, "Strength": 100, "Mana": 200, "Defense": 150},
                 "Jumbo": {"Name": "Jumbo", "Affinity": "Netzach", "Health": 700, "Strength": 125, "Mana": 100, "Defense": 200}}

mini_bosses_moves = {}

bosses = {"Ouroboros Monstrositus": {"Name": "Ouroboros Monstrositus", "Affinity": "Malkhut", "Health": 2000, "Strength": 150, "Mana": 500, "Defense": 200},
          "The Rizzard of zO": {"Name": "The Rizzard of zO", "Affinity": "Yesod", "Health": 2500, "Strength": 200, "Mana": 1000, "Defense": 250},
          "Zorble Zob": {"Name": "Zorble Zob", "Affinity": "Netzach", "Health": 3000, "Strength": 250, "Mana": 1500, "Defense": 300},
          "Jay Jay": {"Name": "Jay Jay", "Affinity": "Netzach", "Health": 4500, "Strength": 300, "Mana": 2000, "Defense": 400},
          "Politician": {"Name": "Politician", "Affinity": "Hod", "Health": 5000, "Strength": 350, "Mana": 2500, "Defense": 500},
          "Paker": {"Name": "Paker", "Affinity": "Hod", "Health": 7500, "Strength": 400, "Mana": 3000, "Defense": 500},
          "PENTIX": {"Name": "PENTIX", "Affinity": "Tiferet", "Health": 10000, "Strength": 450, "Mana": 3500, "Defense": 500},
          "Monarch of the Majestic": {"Name": "Monarch of the Majestic", "Affinity": "Tiferet", "Health": 15000, "Strength": 500, "Mana": 4000, "Defense": 500},
          "Kthululic": {"Name": "Kthululic", "Affinity": "Malkhut", "Health": 20000, "Strength": 600, "Mana": 5000, "Defense": 600}}

bosses_moves = {}


hidden_bosses = {"The Builder": {"Name": "The Builder", "Affinity": "Yesod", "Health": 25000, "Strength": 700, "Mana": 6000, "Defense": 700}}

hidden_bosses_moves = {"The Builder": {"Heavy Duty": {"Damage": 200, "Cost": 200}, "Rumble": {"Damage": 100, "Cost": 100}, "Hammer Strike": {"Damage": 50, "Cost": 50}}}





# Player moves
regular_moves = {"Regular: Shield (Restore/Buff, 0 Mana) [0]": {"Usage": "Restore, Defend", "Cost": 0, "Formula": {"Restore": character["Mana"]/5, "Defend": character["Defense"] * 1.1}, "Description": "A move that anyone can perform."},
                 "Regular: Rest (Restore/Heal, 0 Mana) [11]": {"Usage": "Restore, Heal", "Cost": 0, "Formula": {"Restore": character["Mana"]/7, "Heal": character["Health"]/7}, "Description": "A move that anyonce can perform."}
                 }


malkhut_moves = {"(Link 0) Malkhut: Strike (Single, 0 Mana) [1]": {"Usage": "Damage", "Formula": "Strength * 1", "Cost": 0, "Description": "A basic strike using the power of Malkhut."},
                 "(Link 0) Malkhut: Heavy Strike (Single, 20 Mana) [2]": {"Usage": "Damage", "Formula": "Strength * 2", "Cost": 20, "Description": "A powerful strike using the power of Malkhut."},
                 "(Link 0) Malkhut: Cleave (AOE, 50 Mana) [3]" : {"Usage": "Damage", "Formula": "Strength * 2", "Cost": 50, "Description": "A wide cleave attack using the power of Malkhut."},
                 "(Link 0) Malkhut: Heal Tier 1 (Heal, 15 Mana) [4]": {"Usage": "Heal", "Formula": 25, "Cost": 15, "Description": "Restores health using the widespread power of Malkhut."},
                 "(Link 0) Malkhut: Instant Mana Regen Tier 1 (Restore, 0 Mana) [5]": {"Usage": "Restore", "Formula": 20, "Cost": 0, "Description": "Restores mana using the general power of Malkhut."},
                 "(Link 0) Malkhut: Bullet Strike (Single, 90 Mana) [6]": {"Usage": "Damage", "Formula": "Strength * 3.2", "Cost": 90, "Description": "A high-speed strike using the concentrated power of Malkhut."},
                 "(Link 0) Malkhut: Weapon Up (Buff, 10 Mana) [7]": {"Usage": "Strength_Up", "Formula": 100, "Cost": 10, "Description": "Increases strength using the general power of Malkhut."},
                 "(Link 0) Malkhut: Weapon Rush (Single, 50 Mana) [8]": {"Usage": "Damage", "Formula": "Strength * 2.7", "Cost": 50, "Description": "A rapid sword attack based on the power of Malkhut."},
                 "(Link 0) Malkhut: Earthquake (AOE, 80 Mana) [9]": {"Usage": "Damage", "Formula": "Strength * 3", "Cost": 80, "Description": "A devastating earthquake attack using the full power of Malkhut."},
                 "(Link 0) Malkhut: Surprise Explosion (AOE, 100 Mana) [10]": {"Usage": "Damage", "Formula": "Strength * 3.5", "Cost": 100, "Description": "A surprise explosion attack using the full power of Malkhut."},
                 }

def malkhut_decision(malkhut_move_list, battle_character):
    malkhut_move_list_numbers = []
    for i, move_x in enumerate(malkhut_move_list):
            move_x = (move_x.split("["))[1]
            move_x = move_x.replace("]", "").strip()
            malkhut_move_list_numbers.append(move_x)
    for i, move_x in enumerate(regular_moves):
            move_x = (move_x.split("["))[1]
            move_x = move_x.replace("]", "").strip()
            malkhut_move_list_numbers.append(move_x)

    
    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = malkhut_move_list_numbers[0]
        elif move_x == 2:
            move = malkhut_move_list_numbers[1]
        elif move_x == 3:
            move = malkhut_move_list_numbers[2]
        elif move_x == 4:
            move = malkhut_move_list_numbers[3]
        elif move_x == 5:
            move = malkhut_move_list_numbers[4]
        elif move_x == 0:
            move = malkhut_move_list_numbers[5]
        elif move_x == 11:
            move = malkhut_move_list_numbers[6]


        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character


        elif move == '1':
            move_choice = list(malkhut_moves.keys())[0]
            damage = battle_character["Strength"]
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '2':
            move_choice = list(malkhut_moves.keys())[1]
            damage = battle_character["Strength"] * 2
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '3':
            move_choice = list(malkhut_moves.keys())[2]
            damage = battle_character["Strength"] * 2
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '4':
            move_choice = list(malkhut_moves.keys())[3]
            damage = None
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif battle_character["Health"] >= character["Health"]:
                encounter_text("You are already at full health!")
                continue
            else:
                if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                    battle_character["Health"] += malkhut_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
                else:
                    battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                    battle_character["Health"] += malkhut_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
            
        elif move == '5':
            move_choice = list(malkhut_moves.keys())[4]
            damage = None
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif battle_character["Mana"] >= character["Mana"]:
                encounter_text("You are already at full mana!")
                continue
            else:
                if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                    battle_character["Mana"] += malkhut_moves[move_choice]["Formula"]
                    if battle_character["Mana"] > character["Mana"]:
                        battle_character["Mana"] = character["Mana"]
                    return move_choice, None, "restore", battle_character
                else:
                    battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                    battle_character["Mana"] += malkhut_moves[move_choice]["Formula"]
                    if battle_character["Mana"] > character["Mana"]:
                        battle_character["Mana"] = character["Mana"]
                    return move_choice, None, "restore", battle_character

        elif move == '6':
            move_choice = list(malkhut_moves.keys())[5]
            damage = battle_character["Strength"] * 3.2
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '7':
            move_choice = list(malkhut_moves.keys())[6]
            damage = None
            if battle_character["Buffs"].get("Weapon Up") is not None:
                encounter_text("You already have the buff [Weapon Up] active!")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                battle_character = apply_buff(battle_character, "Weapon Up")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                battle_character = apply_buff(battle_character, "Weapon Up")
                return move_choice, None, "buff", battle_character
        
        elif move == '8':
            move_choice = list(malkhut_moves.keys())[7]
            damage = battle_character["Strength"] * 2.7
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character

        elif move == '9':
            move_choice = list(malkhut_moves.keys())[8]
            damage = battle_character["Strength"] * 3
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
    
        elif move == '10':
            move_choice = list(malkhut_moves.keys())[9]
            damage = battle_character["Strength"] * 3.5
            if malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (malkhut_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character


yesod_moves = {"(Link 1) Yesod: Vessel (AOE, 50 Mana) [1]": {"Usage": "Damage", "Formula": "Strength * 2.5 + character['Health'] - 50", "Cost": 50, "Description": "A powerful attack that uses the pure power of Yesod to strike multiple enemies."},
               "(Link 1) Yesod: Stone Skin (Buff, 100 Mana) [2]": {"Usage": "Defend", "Formula": 50, "Cost": 50, "Description": "Temporarily increases defense."},
               "(Link 1) Yesod: Heal Tier 2 (Heal, 60 Mana) [3]": {"Usage": "Heal", "Formula": 200, "Cost": 60, "Description": "Heals a portion of your health."},
               "(Link 1) Yesod: Mana Regen Tier 2 (Restore, 0 Mana) [4]": {"Usage": "Restore", "Formula": 100, "Cost": 0, "Description": "Restores a portion of your mana."},
               "(Link 1) Yesod: Pierce (Buff, 30 Mana) [5]": {"Usage": "Strength_Up", "Formula": 50, "Cost": 30, "Description": "Increases strength for a short time."},
               "(Link 1) Yesod: Cataclysm (AOE, 300 Mana) [6]": {"Usage": "Damage", "Formula": "Strength * 4 + character['Health'] - 100", "Cost": 150, "Description": "An ultimate attack that uses the full power of Yesod to strike all enemies."},
               "(Link 1) Yesod: Stone Slam (Single, 150 Mana) [7]": {"Usage": "Damage", "Formula": "Strength * 3 + character['Health'] - 75", "Cost": 70, "Description": "A heavy strike that uses the power of Yesod to deal massive damage to a single enemy."},
               "(Link 1) Yesod: Fortify (Buff, 200 Mana) [8]": {"Usage": "Defense_Up", "Formula": 100, "Cost": 200, "Description": "Greatly increases defense for a short time."},
               "(Link 1) Yesod: Grand Heal (Heal, 150 Mana) [9]": {"Usage": "Heal", "Formula": 500, "Cost": 150, "Description": "Heals a large portion of your health."},
               "(Link 1) Yesod: ROAR (AOE, 100 Mana) [10]": {"Usage": "Damage", "Formula": "Strength * 33 / character['Health']", "Cost": 100, "Description": "A roar that strikes all enemies."}
               }

def yesod_decision(yesod_move_list, battle_character):
    yesod_move_list_numbers = []
    for i, move in enumerate(yesod_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            yesod_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            yesod_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character
        
        if move_x == 1:
            move = yesod_move_list_numbers[0]
        elif move_x == 2:
            move = yesod_move_list_numbers[1]
        elif move_x == 3:
            move = yesod_move_list_numbers[2]
        elif move_x == 4:
            move = yesod_move_list_numbers[3]
        elif move_x == 5:
            move = yesod_move_list_numbers[4]
        elif move_x == 0:
            move = yesod_move_list_numbers[5]
        elif move_x == 11:
            move = yesod_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
    
        elif move == '1':
            move_choice = list(yesod_moves.keys())[0]
            damage = battle_character["Strength"] * 2.5 + character["Health"] - 50
            if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= yesod_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character
        
        elif move == '2':
             move_choice = list(yesod_moves.keys())[1]
             damage = None
             if battle_character["Buffs"].get("Stone Skin") is not None:
                encounter_text("You already have the buff [Stone Skin] active!")
                continue
             elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
             elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Stone Skin")
                return move_choice, damage, "buff", battle_character
             else:
                apply_buff(battle_character, "Stone Skin")
                battle_character["Mana"] -= yesod_moves[move_choice]["Cost"]
                return move_choice, damage, "buff", battle_character
        
        elif move == '3':
            move_choice = list(yesod_moves.keys())[2]
            damage = None
            if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif battle_character["Health"] >= character["Health"]:
                encounter_text("You are already at full health!")
                continue
            else:
                if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                    battle_character["Health"] += yesod_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
                else:
                    battle_character["Mana"] -= (yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                    battle_character["Health"] += yesod_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
        
        elif move == '4':
            move_choice = list(yesod_moves.keys())[3]
            damage = None
            if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif battle_character["Mana"] >= character["Mana"]:
                encounter_text("You are already at full mana!")
                continue
            else:
                if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                    battle_character["Mana"] += yesod_moves[move_choice]["Formula"]
                    if battle_character["Mana"] > character["Mana"]:
                        battle_character["Mana"] = character["Mana"]
                    return move_choice, None, "restore", battle_character
                else:
                    battle_character["Mana"] -= (yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                    battle_character["Mana"] += yesod_moves[move_choice]["Formula"]
                    if battle_character["Mana"] > character["Mana"]:
                        battle_character["Mana"] = character["Mana"]
                    return move_choice, None, "restore", battle_character

        elif move == '5':
             move_choice = list(yesod_moves.keys())[4]
             damage = None
             if battle_character["Buffs"].get("Pierce") is not None:
                encounter_text("You already have the buff [Pierce] active!")
                continue
             elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
             elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Pierce")
                return move_choice, damage, "buff", battle_character
             else:
                apply_buff(battle_character, "Pierce")
                battle_character["Mana"] -= yesod_moves[move_choice]["Cost"]
                return move_choice, damage, "buff", battle_character
        
        elif move == '6':
            move_choice = list(yesod_moves.keys())[5]
            damage = battle_character["Strength"] * 4 + character["Health"] - 100
            if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= yesod_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character

        elif move == '7':
            move_choice = list(yesod_moves.keys())[6]
            damage = battle_character["Strength"] * 3 + character["Health"] - 75
            if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= yesod_moves[move_choice]["Cost"]
                return move_choice, damage, "single", battle_character
        
        elif move == '8':
             move_choice = list(yesod_moves.keys())[7]
             damage = None
             if battle_character["Buffs"].get("Fortify") is not None:
                encounter_text("You already have the buff [Fortify] active!")
                continue
             elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
             elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Fortify")
                return move_choice, damage, "buff", battle_character
             else:
                apply_buff(battle_character, "Fortify")
                battle_character["Mana"] -= yesod_moves[move_choice]["Cost"]
                return move_choice, damage, "buff", battle_character
             
        elif move == '9':
            move_choice = list(yesod_moves.keys())[8]
            damage = None
            if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif battle_character["Health"] >= character["Health"]:
                encounter_text("You are already at full health!")
                continue
            else:
                if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                    battle_character["Health"] += yesod_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
                else:
                    battle_character["Mana"] -= (yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                    battle_character["Health"] += yesod_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character

        elif move == '10':
            move_choice = list(yesod_moves.keys())[9]
            damage = battle_character["Strength"] * 33 / character["Health"]
            if yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif yesod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= yesod_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character


hod_moves = {"(Link 1) Hod: Prism Break (Single, 100 Mana) [1]": {"Usage": "Damage", "Formula": "Mana * 3 + 111", "Cost": 100, "Description": "A single target attack channeled through the light of Hod."},
             "(Link 1) Hod: Halo (Buff, 100 Mana) [2]": {"Usage": "Strength_Up, Mana_Up", "Formula(a)": 150, "Formula(b)": 250, "Cost": 100, "Description": "Buffs your mana pool and strength temporarily."},
             "(Link 1) Hod: Refraction (AOE, 150 Mana) [3]": {"Usage": "Damage", "Formula": "Mana * 2.5 + Strength * 1.5 - 111", "Cost": 150, "Description": "A master manipulation of the light of Hod."},
             "(Link 1) Hod: Photon Impulse (Single, 700 Mana) [4]":{"Usage": "Damage", "Formula": "Mana * 8.88", "Cost": 400, "Description": "A high concentration of mana densed into a single beam of light."},
             "(Link 1) Hod: Photon Arc (AOE, 400) [5]": {"Usage": "Damage", "Formula": "Mana * 5.5", "Cost": 400, "Description": "A high concentration of mana densed into a single arc of light."},
             "(Link 1) Hod: Quick Movements (Buff, 200 Mana) [6]": {"Usage": "Buff", "Formula": "Double Dodge Chance", "Cost": 200, "Description": "A blinding flash that reduces the enemy's accuracy."},
             "(Link 1) Hod: Light Speed (Buff, 300 Mana) [7]": {"Usage": "Buff", "Formula": "Double Dodge and Parry Chance", "Cost": 300, "Description": "A burst of light that increases your reaction time."},
             "(Link 1) Hod: Solar Flare (AOE, 500 Mana) [8]": {"Usage": "Damage", "Formula": "Mana * 6 + Strength * 2", "Cost": 500, "Description": "A massive explosion of light that damages all enemies."},
             "(Link 1) Hod: Light Barrier (Buff, 250 Mana) [9]": {"Usage": "Defense_Up", "Formula": 250, "Cost": 250, "Description": "A barrier of light that increases your defense."},
             "(Link 1) Hod: Radiant Burst (AOE, 600 Mana) [10]": {"Usage": "Damage", "Formula": "Mana * 5 + Strength * 3", "Cost": 600, "Description": "A burst of radiant light that damages all enemies."}
             }

def hod_decision(hod_move_list, battle_character):
    hod_move_list_numbers = []
    for i, move in enumerate(hod_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            hod_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            hod_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character
        
        if move_x == 1:
            move = hod_move_list_numbers[0]
        elif move_x == 2:
            move = hod_move_list_numbers[1]
        elif move_x == 3:
            move = hod_move_list_numbers[2]
        elif move_x == 4:
            move = hod_move_list_numbers[3]
        elif move_x == 5:
            move = hod_move_list_numbers[4]
        elif move_x == 0:
            move = hod_move_list_numbers[5]
        elif move_x == 11:
            move = hod_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(hod_moves.keys())[0]
            damage = battle_character["Mana"] * 3 + 111
            if hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                return move_choice, damage, "single", battle_character
        
        elif move == '2':
            move_choice = list(hod_moves.keys())[1]
            damage = None
            if battle_character["Buffs"].get("Halo") is not None:
                encounter_text("You already have the buff [Halo] active!")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Halo")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Halo")
                return move_choice, damage, "buff", battle_character
        
        elif move == '3':
            move_choice = list(hod_moves.keys())[2]
            damage = battle_character["Mana"] * 2.5 + battle_character["Strength"] * 1.5 - 111
            if hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character
        
        elif move == '4':
            move_choice = list(hod_moves.keys())[3]
            damage = battle_character["Mana"] * 8.88
            if hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                return move_choice, damage, "single", battle_character
        
        elif move == '5':
            move_choice = list(hod_moves.keys())[4]
            damage = battle_character["Mana"] * 5.5
            if hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character
        
        elif move == '6':
            move_choice = list(hod_moves.keys())[5]
            damage = None
            if battle_character["Buffs"].get("Quick Movements") is not None:
                encounter_text("You already have the buff [Quick Movements] active!")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Blinding Light")
                return move_choice, damage, "debuff", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Blinding Light")
                return move_choice, damage, "debuff", battle_character
            
        elif move == '7':
            move_choice = list(hod_moves.keys())[6]
            damage = None
            if battle_character["Buffs"].get("Light Speed") is not None:
                encounter_text("You already have the buff [Light Speed] active!")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Light Speed")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Light Speed")
                return move_choice, damage, "buff", battle_character
        
        elif move == '8':
            move_choice = list(hod_moves.keys())[7]
            damage = battle_character["Mana"] * 6 + battle_character["Strength"] * 2
            if hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character
        
        elif move == '9':
            move_choice = list(hod_moves.keys())[8]
            damage = None
            if battle_character["Buffs"].get("Light Barrier") is not None:
                encounter_text("You already have the buff [Light Barrier] active!")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Light Barrier")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Light Barrier")
                return move_choice, damage, "buff", battle_character
        
        elif move == '10':
            move_choice = list(hod_moves.keys())[9]
            damage = battle_character["Mana"] * 5 + battle_character["Strength"] * 3
            if hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif hod_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= hod_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character


netzach_moves = {"(Link 1) Netzach: Overtake (Single, 350 Mana) [1]": {"Usage": "Damage", "Formula": "Strength * 3 + Mana * 1.5 + 77", "Cost": 350, "Description": "A powerful strike that uses the overwhelming force of Netzach to crush a single enemy."},
                  "(Link 1) Netzach: Last Stand (Buff, 500 Mana) [2]": {"Usage": "Buff", "Formula": "+100 Defense and then Doubles Defense", "Cost": 500, "Description": "A defensive stance that grants a temporary boost to defense."},
                  "(Link 1) Netzach: Bash (Single, 250 Mana) [3]": {"Usage": "Damage", "Formula": "Defense * 5 + Strength * 1.5", "Cost": 250, "Description": "A powerful blow that deals damage based on the character's defense and strength."},
                  "(Link 1) Netzach: Overchain (AOE, 300 Mana) [4]": {"Usage": "Damage", "Formula": "Strength * 3 + 99", "Cost": 300, "Description": "A devastating attack that affects all enemies in the area."},
                  "(Link 1) Netzach: Overdrive (AOE, 750 Mana) [5]": {"Usage": "Damage", "Formula": "Strength * 5 + Mana * 3", "Cost": 750, "Description": "A powerful attack that overloads enemies with a surge of strength and mana."},
                  "(Link 1) Netzach: Overclock (Buff, 500 Mana) [6]": {"Usage": "Buff", "Formula": "Doubles Strength", "Cost": 500, "Description": "A surge of power that temporarily doubles the character's strength."},
                  "(Link 1) Netzach: Overload (Buff, 500 Mana) [7]": {"Usage": "Buff", "Formula": "Doubles Mana", "Cost": 500, "Description": "A surge of power that temporarily doubles the character's mana."},
                  "(Link 1) Netzach: Overpower (Single, 1000 Mana) [8]": {"Usage": "Damage", "Formula": "Strength * 15 + Mana * 5 - Defense * 10", "Cost": 1000, "Description": "An ultimate attack that unleashes the full power of Netzach to crush a single enemy."},
                  "(Link 1) Netzach: King of the Hill (Buff, 1000 Mana) [9]": {"Usage": "Buff", "Formula": "+500 Defense and then Defense times 1.25", "Cost": 1000, "Description": "A powerful stance that grants a temporary boost to both strength and defense."},
                  "(Link 1) Netzach: Eternal Victory (AOE, 1250 Mana) [10]": {"Usage": "Damage", "Formula": "Strength * 10 + Mana * 5 + 500", "Cost": 1250, "Description": "An ultimate attack that unleashes the full power of Netzach to crush all enemies in the area."}}

def netzach_decision(netzach_move_list, battle_character):
    netzach_move_list_numbers = []
    for i, move in enumerate(netzach_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            netzach_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            netzach_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = netzach_move_list_numbers[0]
        elif move_x == 2:
            move = netzach_move_list_numbers[1]
        elif move_x == 3:
            move = netzach_move_list_numbers[2]
        elif move_x == 4:
            move = netzach_move_list_numbers[3]
        elif move_x == 5:
            move = netzach_move_list_numbers[4]
        elif move_x == 0:
            move = netzach_move_list_numbers[5]
        elif move_x == 11:
            move = netzach_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(netzach_moves.keys())[0]
            damage = battle_character["Strength"] * 3 + battle_character["Mana"] * 1.5 + 77
            if netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                return move_choice, damage, "single", battle_character
        
        elif move == '2':
            move_choice = list(netzach_moves.keys())[1]
            damage = None
            if battle_character["Buffs"].get("Last Stand") is not None:
                encounter_text("You already have the buff [Last Stand] active!")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Last Stand")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Last Stand")
                return move_choice, damage, "buff", battle_character
        
        elif move == '3':
            move_choice = list(netzach_moves.keys())[2]
            damage = battle_character["Defense"] * 5 + battle_character["Strength"] * 1.5
            if netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                return move_choice, damage, "single", battle_character
        
        elif move == '4':
            move_choice = list(netzach_moves.keys())[3]
            damage = battle_character["Strength"] * 3 + 99
            if netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character
        
        elif move == '5':
            move_choice = list(netzach_moves.keys())[4]
            damage = battle_character["Strength"] * 5 + battle_character["Mana"] * 3
            if netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character
        
        elif move == '6':
            move_choice = list(netzach_moves.keys())[5]
            damage = None
            if battle_character["Buffs"].get("Overclock") is not None:
                encounter_text("You already have the buff [Overclock] active!")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Overclock")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Overclock")
                return move_choice, damage, "buff", battle_character
        
        elif move == '7':
            move_choice = list(netzach_moves.keys())[6]
            damage = None
            if battle_character["Buffs"].get("Overload") is not None:
                encounter_text("You already have the buff [Overload] active!")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Overload")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Overload")
                return move_choice, damage, "buff", battle_character
        
        elif move == '8':
            move_choice = list(netzach_moves.keys())[7]
            damage = battle_character["Strength"] * 15 + battle_character["Mana"] * 5 - battle_character["Defense"] * 10
            if netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                return move_choice, damage, "single", battle_character
            
        elif move == '9':
            move_choice = list(netzach_moves.keys())[8]
            damage = None
            if battle_character["Buffs"].get("King of the Hill") is not None:
                encounter_text("You already have the buff [King of the Hill] active!")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "King of the Hill")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                apply_buff(battle_character, "King of the Hill")
                return move_choice, damage, "buff", battle_character
        
        elif move == '10':
            move_choice = list(netzach_moves.keys())[9]
            damage = battle_character["Strength"] * 10 + battle_character["Mana"] * 5 + 500
            if netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif netzach_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= netzach_moves[move_choice]["Cost"]
                return move_choice, damage, "aoe", battle_character


tiferet_moves = {"(Link 2) Tiferet: Perfect Form (Buff, 1250 Mana) [1]": {"Usage": "Buff", "Formula": "Mana, Strength, Defense, Health: +1250", "Cost": 1250, "Description": "A powerful buff that enhances most of the user's main attributes"},
                 "(Link 2) Tiferet: Heal Tier 3 (Heal, 500 Mana) [2]": {"Usage": "Heal", "Formula": 5000, "Cost": 500, "Description": "A greatly enhanced healing move."},
                 "(Link 2) Tiferet: Mana Regen Tier 3 (Restore, 0 Mana) [3]": {"Usage": "Restore", "Formula": 5000, "Cost": 0, "Description": "A greatly enhanced mana restoring move."},
                 "(Link 2) Tiferet: Beacon (AOE, 999 Mana) [4]": {"Usage": "Damage", "Formula": "Mana * 5 + Strength * 4", "Cost": 999, "Description": "A move that shoots out a multicolored beacon from your hands."},
                 "(Link 2) Tiferet: Miracle (Buff, 1 Mana) [5]": {"Usage": "Buff", "Formula": "Adds 10,000 Defense", "Cost": 1, "Description": "A miracle-calling move that strengthens your defense so that you may last just even one more attack."},
                 "(Link 2) Tiferet: Integration (AOE, 2000 Mana) [6]": {"Usage": "Damage", "Formula": "5555 * number_of_enemies", "Cost": 2000, "Description": "A move that calls upon a constricting force."},
                 "(Link 2) Tiferet: Coordination (Single, 1540 Mana) [7]": {"Usage": "Damage", "Formula": "Sum of character's coordinates * 9.5", "Cost": 1540, "Description": "A single target strike that increases with power based on where you are relative to the center of the world."},
                 "(Link 2) Tiferet: Unity Flow (AOE, 450 Mana) [8]": {"Usage": "Damage", "Formula": "Mana * 4.5 + 2000 - Defense", "Cost": 450, "Description": "A flowing move that cuts through all targets in range."},
                 "(Link 2) Tiferet: Form's Beauty (AOE, 0 Mana) [9]": {"Usage": "Damage", "Formula": "10,000,000 / (Defense - Mana + Health - Strength)", "Cost": 0, "Description": "An extremely powerful move that scales based on how balanced your main attributes are."},
                 "(Link 2) Tiferet: Beauty of Form (Single, 0 Mana) [10]": {"Usage": "Damage", "Formula": "10,000,000 / (Mana - Defense + Strength - Health)", "Cost": 0, "Description": "An extremely powerful move that scales based on how balanced your main attributes are."}}

def tiferet_decision(tiferet_move_list, battle_character, battle_enemy_list):
    global character
    tiferet_move_list_numbers = []
    for i, move in enumerate(tiferet_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            tiferet_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            tiferet_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = tiferet_move_list_numbers[0]
        elif move_x == 2:
            move = tiferet_move_list_numbers[1]
        elif move_x == 3:
            move = tiferet_move_list_numbers[2]
        elif move_x == 4:
            move = tiferet_move_list_numbers[3]
        elif move_x == 5:
            move = tiferet_move_list_numbers[4]
        elif move_x == 0:
            move = tiferet_move_list_numbers[5]
        elif move_x == 11:
            move = tiferet_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(tiferet_moves.keys())[0]
            damage = None
            if battle_character["Buffs"].get("Perfect Form") is not None:
                encounter_text("You already have the buff [Perfect Form] active!")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Perfect Form")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= tiferet_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Perfect Form")
                return move_choice, damage, "buff", battle_character
        
        elif move == '2':
            move_choice = list(tiferet_moves.keys())[1]
            damage = None
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif battle_character["Health"] >= character["Health"]:
                encounter_text("You are already at full health!")
                continue
            else:
                if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                    battle_character["Health"] += tiferet_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
                else:
                    battle_character["Mana"] -= (tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                    battle_character["Health"] += tiferet_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
        
        elif move == '3':
            move_choice = list(tiferet_moves.keys())[4]
            damage = None
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif battle_character["Mana"] >= character["Mana"]:
                encounter_text("You are already at full mana!")
                continue
            else:
                if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                    battle_character["Mana"] += tiferet_moves[move_choice]["Formula"]
                    if battle_character["Mana"] > character["Mana"]:
                        battle_character["Mana"] = character["Mana"]
                    return move_choice, None, "restore", battle_character
                else:
                    battle_character["Mana"] -= (tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                    battle_character["Mana"] += tiferet_moves[move_choice]["Formula"]
                    if battle_character["Mana"] > character["Mana"]:
                        battle_character["Mana"] = character["Mana"]
                    return move_choice, None, "restore", battle_character
        
        elif move == '4':
            move_choice = list(tiferet_moves.keys())[3]
            damage = (battle_character["Strength"] * 4) + (battle_character["Mana"] * 5)
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '5':
            move_choice = list(tiferet_moves.keys())[4]
            damage = None
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Miracle")
                battle_character["Mana"] += 3000
                if battle_character["Mana"] > character["Mana"]:
                    battle_character["Mana"] = character["Mana"]
                return move_choice, damage, ["buff", "restore"], battle_character
            else:
                battle_character["Mana"] -= tiferet_moves[move_choice]["Cost"]
                apply_buff(battle_character, "Miracle")
                battle_character["Mana"] += 3000
                if battle_character["Mana"] > character["Mana"]:
                    battle_character["Mana"] = character["Mana"]
                return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '6':
            move_choice = list(tiferet_moves.keys())[5]
            damage = 5555 * len(list(battle_enemy_list.keys()))
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '7':
            move_choice = list(tiferet_moves.keys())[6]
            damage = (abs(battle_character["Coordinates"][0]) + abs(battle_character["Coordinates"][1])) * 9.5
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '8':
            move_choice = list(tiferet_moves.keys())[7]
            damage = battle_character["Mana"] * 4.5 + 2000 - battle_character["Defense"]
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
            
        elif move == '9':
            move_choice = list(tiferet_moves.keys())[8]
            damage = 10000000 / (battle_character["Defense"] - battle_character["Mana"] + battle_character["Health"] - battle_character["Strength"])
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '10':
            move_choice = list(tiferet_moves.keys())[9]
            damage = 10000000 / (battle_character["Mana"] - battle_character["Defense"] - battle_character["Health"] + battle_character["Strength"])
            if tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (tiferet_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character


chesed_moves = {"(Link 2) Chesed: Divine Mercy (Heal, 1250 Mana) [1]": {"Usage": "Heal", "Formula": 12500, "Cost": 1250, "Description": "A powerful healing move that calls upon the mercy of Chesed to restore a large amount of health."},
                "(Link 2) Chesed: Sanctify (AOE, 800 Mana) [2]": {"Usage": "Damage", "Formula": "Health * 8 + Defense - Strength * 0.3", "Cost": 800, "Description": "A holy strike that damages all enemies in the area."},
                "(Link 2) Chesed: Aegis (Single, 1000 Mana) [3]": {"Usage": "Damage", "Formula": "Health * 11 + Defense * 3", "Cost": 1000, "Description": "A powerful strike that uses the user's health and defense to deal damage to a single enemy."},
                "(Link 2) Chesed: Holy Shield (Buff, 1500 Mana) [4]": {"Usage": "Buff", "Formula": "Triples Defense", "Cost": 1500, "Description": "A powerful defensive move that greatly increases the user's defense."},
                "(Link 2) Chesed: Holy Halo (Buff, 1300 Mana) [5]": {"Usage": "Buff", "Formula": "Doubles Health", "Cost": 1300, "Description": "A protective move that greatly increases the user's health."},
                "(Link 2) Chesed: Mana Halo (Buff, 2000 Mana) [6]": {"Usage": "Buff", "Formula": "Triples Mana", "Cost": 2000, "Description": "A powerful move that greatly increases the user's mana."},
                "(Link 2) Chesed: Indestructible (Buff, 2500 Mana) [7]": {"Usage": "Buff", "Formula": "Doubles Health, Triples Defense", "Cost": 2500, "Description": "An ultimate defensive move that greatly increases both the user's health and defense."},
                "(Link 2) Chesed: Mana Shield (Buff, Half of Mana) [8]": {"Usage": "Buff", "Formula": "Converts half of Mana to Defense, then multiply defense by 5", "Cost": "Half of Mana", "Description": "A defensive move that converts a portion of the user's mana into defense."},
                "(Link 2) Chesed: Rhythm (Buff, 0 Mana) [9]": {"Usage": "Strength_Up", "Formula": "Increases Strength randomly", "Cost": 0, "Description": "A move that increases the user's attack greatly."},
                "(Link 2) Chesed: Divine Rhythm (Buff, 0 Mana) [10]": {"Usage": "Strength_Up", "Formula": "Increases Strength randomly", "Cost": 0, "Description": "A move that greatly increases the user's attack."}}

def chesed_decision(chesed_move_list, battle_character):
    global character
    chesed_move_list_numbers = []
    for i, move in enumerate(chesed_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            chesed_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            chesed_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = chesed_move_list_numbers[0]
        elif move_x == 2:
            move = chesed_move_list_numbers[1]
        elif move_x == 3:
            move = chesed_move_list_numbers[2]
        elif move_x == 4:
            move = chesed_move_list_numbers[3]
        elif move_x == 5:
            move = chesed_move_list_numbers[4]
        elif move_x == 0:
            move = chesed_move_list_numbers[5]
        elif move_x == 11:
            move = chesed_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(chesed_moves.keys())[0]
            damage = None
            if chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif battle_character["Health"] >= character["Health"]:
                encounter_text("You are already at full health!")
                continue
            else:
                if chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                    battle_character["Health"] += chesed_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
                else:
                    battle_character["Mana"] -= (chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                    battle_character["Health"] += chesed_moves[move_choice]["Formula"]
                    if battle_character["Health"] > character["Health"]:
                        battle_character["Health"] = character["Health"]
                    return move_choice, None, "heal", battle_character
        
        elif move == '2':
            move_choice = list(chesed_moves.keys())[1]
            damage = battle_character["Health"] * 8 + battle_character["Defense"] - battle_character["Strength"] * 0.3
            if chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '3':
            move_choice = list(chesed_moves.keys())[2]
            damage = battle_character["Health"] * 11 + battle_character["Defense"] * 3
            if chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
            
        elif move == '4':
            move_choice = list(chesed_moves.keys())[3]
            damage = None
            if battle_character["Buffs"].get("Holy Shield") is not None:
                encounter_text("You already have the buff [Holy Shield] active!")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Holy Shield")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Holy Shield")
                return move_choice, damage, "buff", battle_character

        elif move == '5':
            move_choice = list(chesed_moves.keys())[4]
            damage = None
            if battle_character["Buffs"].get("Holy Halo") is not None:
                encounter_text("You already have the buff [Holy Halo] active!")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Holy Halo")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Holy Halo")
                return move_choice, damage, "buff", battle_character

        elif move == '6':
            move_choice = list(chesed_moves.keys())[5]
            damage = None
            if battle_character["Buffs"].get("Mana Halo") is not None:
                encounter_text("You already have the buff [Mana Halo] active!")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Mana Halo")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Mana Halo")
                return move_choice, damage, "buff", battle_character

        elif move == '7':
            move_choice = list(chesed_moves.keys())[6]
            damage = None
            if battle_character["Buffs"].get("Indestructible") is not None:
                encounter_text("You already have the buff [Indestructible] active!")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Indestructible")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chesed_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Indestructible")
                return move_choice, damage, "buff", battle_character
            
        elif move == '8':
            move_choice = list(chesed_moves.keys())[7]
            damage = None
            battle_character["Mana"] /= 2
            apply_buff(battle_character, "Mana Shield")
            return move_choice, damage, "buff", battle_character

        elif move == '9':
            move_choice = list(chesed_moves.keys())[8]
            damage = None
            apply_buff(battle_character, "Rhythm")
            return move_choice, damage, "buff", battle_character

        elif move == '10':
            move_choice = list(chesed_moves.keys())[9]
            damage = None
            apply_buff(battle_character, "Divine Rhythm")
            return move_choice, damage, "buff", battle_character


gevurah_moves = {"(Link 2) Gevurah: Iron Decree (Single, 1250 Mana) [1]": {"Usage": "Damage", "Formula": 17000, "Cost": 1250, "Description": "A powerful strike."},
                 "(Link 2) Gevurah: Steel Covenant (AOE, 1000 Mana) [2]": {"Usage": "Damage", "Formula": 12000, "Cost": 1000, "Description": "A sturdy attack."},
                 "(Link 2) Gevurah: Titanium Strike (Single, 1500 Mana) [3]": {"Usage": "Damage", "Formula": "Strength * 10 + Mana * 5", "Cost": 1500, "Description": "A devastating strike that harnesses the user's strength and mana."},
                 "(Link 2) Gevurah: Absolute Strike (Single, 1750 Mana) [4]": {"Usage": "Damage", "Formula": "Strength * 5 + Mana * 10", "Cost": 1750, "Description": "An overwhelming attack that utilizes the user's full strength and mana."},
                 "(Link 2) Gevurah: Godstep (Single, 2000 Mana) [5]": {"Usage": "Damage", "Formula": "Strength * 10 + Mana * 10", "Cost": 2000, "Description": "A divine step that deals massive damage using the user's strength and mana."},
                 "(Link 2) Gevruah: Wrath of the King (AOE, 2250 Mana) [6]": {"Usage": "Damage", "Formula": "Defense * 25", "Cost": 2250, "Description": "The king's fury that unleashes tremendous damage through the user's defense stat."},
                 "(Link 2) Gevurah: Absolute Kingstep (AOE, 2500 Mana) [7]": {"Usage": "Damage", "Formula": "(Strength * 10 + Mana * 10) / (Defense / 1000)", "Cost": 2500, "Description": "A powerful step that combines the user's strength, mana, and low defense."},
                 "(Link 2) Gevurah: Absolute Godstep (Single, 2750 Mana) [8]": {"Usage": "Damage", "Formula": "(Mana * 15) / (Strength / 10000)", "Cost": 2750, "Description": "A divine step that deals massive damage using the user's strength and mana."},
                 "(Link 2) Gevurah: The Last Strike (AOE, 3000 Mana) [9]": {"Usage": "Damage", "Formula": "sqrt(Strength + Mana) * 155", "Cost": 3000, "Description": "Consecutive strikes that utilizes the user's full strength and mana."},
                 "(Link 2) Gevurah: The Final Strike (Single, 3250 Mana) [10]": {"Usage": "Damage", "Formula": "sqrt(Strength**2 + Mana**2) * 1.5", "Cost": 3250, "Description": "The final strike that deals tremendous damage using the user's strength and mana."}}

def gevurah_decision(gevurah_move_list, battle_character):
    global character
    gevurah_move_list_numbers = []
    for i, move in enumerate(gevurah_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            gevurah_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            gevurah_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = gevurah_move_list_numbers[0]
        elif move_x == 2:
            move = gevurah_move_list_numbers[1]
        elif move_x == 3:
            move = gevurah_move_list_numbers[2]
        elif move_x == 4:
            move = gevurah_move_list_numbers[3]
        elif move_x == 5:
            move = gevurah_move_list_numbers[4]
        elif move_x == 0:
            move = gevurah_move_list_numbers[5]
        elif move_x == 11:
            move = gevurah_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(gevurah_moves.keys())[0]
            damage = 17000
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '2':
            move_choice = list(gevurah_moves.keys())[1]
            damage = 12000
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '3':
            move_choice = list(gevurah_moves.keys())[2]
            damage = battle_character["Strength"] * 10 + battle_character["Mana"] * 5
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character

        elif move == '4':
            move_choice = list(gevurah_moves.keys())[3]
            damage = battle_character["Strength"] * 5 + battle_character["Mana"] * 10
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '5':
            move_choice = list(gevurah_moves.keys())[4]
            damage = battle_character["Strength"] * 10 + battle_character["Mana"] * 10
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '6':
            move_choice = list(gevurah_moves.keys())[5]
            damage = battle_character["Defense"] * 25
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character

        elif move == '7':
            move_choice = list(gevurah_moves.keys())[6]
            damage = (battle_character["Strength"] * 10 + battle_character["Mana"] * 10) / (battle_character["Defense"] / 1000)
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '8':
            move_choice = list(gevurah_moves.keys())[7]
            damage = (battle_character["Mana"] * 15) / (battle_character["Strength"] / 10000)
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '9':
            move_choice = list(gevurah_moves.keys())[8]
            damage = math.sqrt(battle_character["Strength"] + battle_character["Mana"]) * 155
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '10':
            move_choice = list(gevurah_moves.keys())[9]
            damage = math.sqrt(battle_character["Strength"]**2 + battle_character["Mana"]**2) * 1.5
            if gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (gevurah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character


chokmah_moves = {"(Link 3) Chokmah: Flash Insight (Buff, 2500 Mana) [1]": {"Usage": "Buff", "Formula": "Increases Wisdom randomly", "Cost": 2500, "Description": "A move that increases the user's wisdom greatly."},
                 "(Link 3) Chokmah: Primal Bolt (Single, 1500 Mana) [2]": {"Usage": "Single", "Formula": "Strength * Mana / 1000", "Cost": 1500, "Description": "A powerful single-target attack for a low mana cost."},
                 "(Link 3) Chokmah: Infinite Radiance (AOE, 3000 Mana) [3]": {"Usage": "AOE", "Formula": "Strength * Defense / (Mana / 30000)", "Cost": 3000, "Description": "A devastating area-of-effect attack."},
                 "(Link 3) Chokmah: Primordial Sight (Buff, 5000 Mana) [4]": {"Usage": "Buff", "Formula": "Increases critical hit chance", "Cost": 5000, "Description": "A move that enhances the user's critical hit potential."},
                 "(Link 3) Chokmah: Divine Overclock (Buff, 5000 Mana) [5]": {"Usage": "Buff", "Formula": "Increases Mana", "Cost": 5000, "Description": "A move that boosts the user's attack speed."},
                 "(Link 3) Chokmah: Divine Overdrive (Buff, 5000 Mana) [6]": {"Usage": "Buff", "Formula": "Increases Strength", "Cost": 5000, "Description": "A move that significantly increases the user's damage output."},
                 "(Link 3) Chokmah: Emanation (AOE, 4000 Mana) [7]": {"Usage": "AOE", "Formula": "Strength * 500 / (Mana / 30000)", "Cost": 4000, "Description": "A devastating area-of-effect attack."},
                 "(Link 3) Chokmah: Infinite Insight (Buff, 5000 Mana) [8]": {"Usage": "Buff", "Formula": "Greatly increases Wisdom randomly", "Cost": 5000, "Description": "A move that increases the user's wisdom greatly."},
                 "(Link 3) Chokmah: Divine Focus (Buff, 1 Mana) [9]": {"Usage": "Buff", "Formula": "Increases Crit, Dodge, and Luck randomly", "Cost": 1, "Description": "A move that enhances the user's mana."},
                 "(Link 3) Chokmah: Absolute Focus (Buff, 1 Mana) [10]": {"Usage": "Buff", "Formula": "Greatly increases Crit, Dodge, and Luck randomly", "Cost": 1, "Description": "A move that boosts the user's mana."}}

def chokmah_decision(chokmah_move_list, battle_character):
    global character
    chokmah_move_list_numbers = []
    for i, move in enumerate(chokmah_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            chokmah_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            chokmah_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = chokmah_move_list_numbers[0]
        elif move_x == 2:
            move = chokmah_move_list_numbers[1]
        elif move_x == 3:
            move = chokmah_move_list_numbers[2]
        elif move_x == 4:
            move = chokmah_move_list_numbers[3]
        elif move_x == 5:
            move = chokmah_move_list_numbers[4]
        elif move_x == 0:
            move = chokmah_move_list_numbers[5]
        elif move_x == 11:
            move = chokmah_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(chokmah_moves.keys())[0]
            damage = None
            if battle_character["Buffs"].get("Flash Insight") is not None:
                encounter_text("You already have the buff [Flash Insight] active!")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Flash Insight")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Flash Insight")
                return move_choice, damage, "buff", battle_character

        elif move == '2':
            move_choice = list(chokmah_moves.keys())[1]
            damage = battle_character["Strength"] * battle_character["Mana"] / 1000
            if chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character

        elif move == '3':
            move_choice = list(chokmah_moves.keys())[2]
            damage = battle_character["Strength"] * battle_character["Defense"] / (battle_character["Mana"] / 30000)
            if chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '4':
            move_choice = list(chokmah_moves.keys())[3]
            damage = None
            if battle_character["Buffs"].get("Primordial Sight") is not None:
                encounter_text("You already have the buff [Primordial Sight] active!")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Primordial Sight")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Primordial Sight")
                return move_choice, damage, "buff", battle_character

        elif move == '5':
            move_choice = list(chokmah_moves.keys())[4]
            damage = None
            if battle_character["Buffs"].get("Divine Overclock") is not None:
                encounter_text("You already have the buff [Divine Overclock] active!")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Divine Overclock")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Divine Overclock")
                return move_choice, damage, "buff", battle_character

        elif move == '6':
            move_choice = list(chokmah_moves.keys())[5]
            damage = None
            if battle_character["Buffs"].get("Divine Overdrive") is not None:
                encounter_text("You already have the buff [Divine Overdrive] active!")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Divine Overdrive")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Divine Overdrive")
                return move_choice, damage, "buff", battle_character
        
        elif move == '7':
            move_choice = list(chokmah_moves.keys())[6]
            damage = battle_character["Strength"] * 500 / (battle_character["Mana"] / 30000)
            if chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character

        elif move == '8':
            move_choice = list(chokmah_moves.keys())[7]
            damage = None
            if battle_character["Buffs"].get("Infinite Insight") is not None:
                encounter_text("You already have the buff [Infinite Insight] active!")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Infinite Insight")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Infinite Insight")
                return move_choice, damage, "buff", battle_character
            
        elif move == '9':
            move_choice = list(chokmah_moves.keys())[8]
            damage = None
            if battle_character["Buffs"].get("Divine Focus") is not None:
                encounter_text("You already have the buff [Divine Focus] active!")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Divine Focus")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Divine Focus")
                return move_choice, damage, "buff", battle_character
        
        elif move == '10':
            move_choice = list(chokmah_moves.keys())[9]
            damage = None
            if battle_character["Buffs"].get("Absolute Focus") is not None:
                encounter_text("You already have the buff [Divine Focus] active!")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Absolute Focus")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Absolute Focus")
                return move_choice, damage, "buff", battle_character


binah_moves = {"(Link 3) Binah: Impulse Arc (AOE, 3000 Mana) [1]": {"Usage": "Damage", "Formula": "(Mana**2 / Strength) * 50", "Cost": 3000, "Description": "A devastating area-of-effect attack."},
               "(Link 3) Binah: Arcing Impulse (AOE, 2200 Mana) [2]": {"Usage": "Damage", "Formula": "(Strength**2 / Mana) * 50", "Cost": 2200, "Description": "A powerful area-of-effect attack."},
               "(Link 3) Binah: Structation (Buff, 2000 Mana) [3]": {"Usage": "Buff", "Formula": "Increases Defense randomly", "Cost": 2000, "Description": "A move that increases the user's defense greatly."},
               "(Link 3) Binah: Templarism (Single, 3333 Mana) [4]": {"Usage": "Damage", "Formula": "(Defense**2 / (Critical + Dodge + 10)) * 50", "Cost": 3333, "Description": "A powerful single-target attack that utilizes the user's defense."},
               "(Link 3) Binah: The Great Throne (AOE, 3333 Mana) [5]": {"Usage": "Damage", "Formula": "(Critical + Dodge + 10)**2) * 200", "Cost": 3333, "Description": "A devastating area-of-effect attack that utilizes the user's critical hit chance and dodge."},
               "(Link 3) Binah: Crossing of the Sands (AOE, 7777 Mana) [6]": {"Usage": "Damage", "Formula": "round(Sum of character's coordinates * 777)", "Cost": 7777, "Description": "A powerful area-of-effect attack."},
               "(Link 3) Binah: The Seventh Light (Buff, 5555 Mana) [7]": {"Usage": "Buff", "Formula": "Increases all stats randomly", "Cost": 5555, "Description": "A move that increases all of the user's stats greatly."},
               "(Link 3) Binah: Perfect Execution (Single, 5000 Mana) [8]": {"Usage": "Damage", "Formula": 1000000, "Cost": 5000, "Description": "A powerful single-target attack."},
               "(Link 3) Binah: Perfect Defense (Buff, 5000 Mana) [9]": {"Usage": "Buff", "Formula": "Adds 10000 to Defense, then 3.5x it.", "Cost": 5000, "Description": "A move that greatly increases the user's defense."},
               "(Link 3) Binah: Perfect Attack (Single, 5555 Mana) [10]": {"Usage": "Damage", "Formula": "((Mana**2 / Strength) * 50 + (Strength**2 / Mana) * 50) * 1.222", "Cost": 5555, "Description": "A powerful single-target attack."}}

def binah_decision(binah_move_list, battle_character):
    global character
    binah_move_list_numbers = []
    for i, move in enumerate(binah_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            binah_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            binah_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = binah_move_list_numbers[0]
        elif move_x == 2:
            move = binah_move_list_numbers[1]
        elif move_x == 3:
            move = binah_move_list_numbers[2]
        elif move_x == 4:
            move = binah_move_list_numbers[3]
        elif move_x == 5:
            move = binah_move_list_numbers[4]
        elif move_x == 0:
            move = binah_move_list_numbers[5]
        elif move_x == 11:
            move = binah_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(binah_moves.keys())[0]
            damage = battle_character["Mana"]**2 / battle_character["Strength"] * 50
            if binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '2':
            move_choice = list(binah_moves.keys())[1]
            damage = battle_character["Strength"]**2 / battle_character["Mana"] * 50
            if binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '3':
            move_choice = list(binah_moves.keys())[2]
            damage = None
            if battle_character["Buffs"].get("Structation") is not None:
                encounter_text("You already have the buff [Structation] active!")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Structation")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (binah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Structation")
                return move_choice, damage, "buff", battle_character
        
        elif move == '4':
            move_choice = list(chokmah_moves.keys())[3]
            damage = battle_character["Defense"]**2 / (battle_character["Critical"] + battle_character["Dodge"] + 10) * 50
            if chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '5':
            move_choice = list(binah_moves.keys())[4]
            damage = (battle_character["Critical"] + battle_character["Dodge"] + 10)**2 * 200
            if binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character

        elif move == '6':
            move_choice = list(binah_moves.keys())[5]
            damage = round(abs(battle_character["Coordinates"][0]) + abs(battle_character["Coordinates"][1])) * 777
            if binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character

        elif move == '7':
            move_choice = list(binah_moves.keys())[6]
            damage = None
            if battle_character["Buffs"].get("The Seventh Light") is not None:
                encounter_text("You already have the buff [The Seventh Light] active!")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "The Seventh Light")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (binah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "The Seventh Light")
                return move_choice, damage, "buff", battle_character
        
        elif move == '8':
            move_choice = list(chokmah_moves.keys())[7]
            damage = 1000000
            if chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '9':
            move_choice = list(binah_moves.keys())[8]
            damage = None
            if battle_character["Buffs"].get("Perfect Defense") is not None:
                encounter_text("You already have the buff [Perfect Defense] active!")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif binah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Perfect Defense")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (binah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Perfect Defense")
                return move_choice, damage, "buff", battle_character
        
        elif move == '10':
            move_choice = list(chokmah_moves.keys())[9]
            damage = ((battle_character["Mana"]**2 / battle_character["Strength"]) * 50 + (battle_character["Strength"]**2 / battle_character["Mana"]) * 50) * 1.222
            if chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (chokmah_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character


keter_moves = {"(Link 4) Keter: King's Stride (Single, 9999 Mana) [1]": {"Usage": "Damage", "Formula": "Strength * Mana / 7", "Cost": 9999, "Description": "A attack that strikes the enemy with great force in a short amount of time."},
               "(Link 4) Keter: Blade Ascension (Single, 12000) [2]": {"Usage": "Damage", "Formula": 5000000, "Cost": 12000, "Description": "A powerful single-target attack that deals massive damage."},
               "(Link 4) Keter: Heavenrend (AOE, 15000) [3]": {"Usage": "Damage", "Formula": "Strength * Mana / 7", "Cost": 15000, "Description": "A devastating area-of-effect attack utilizing the user's mana and affinity with Keter."},
               "(Link 4) Keter: Will of the Crown (Buff, 25000) [4]": {"Usage": "Buff", "Formula": "Increases ALL stats, then multiplies ALL stats by five", "Cost": 25000, "Description": "Increases ALL stats."},
               "(Link 4) Keter: Absolute Judgment (AOE, 30000) [5]": {"Usage": "Damage", "Formula": "Strength * Mana * Health / (abs(Wisdom * Defense - 1000) + 1)", "Cost": 30000, "Description": "The third most powerful attack in the game."}}

def keter_decision(keter_move_list, battle_character):
    global character
    keter_move_list_numbers = []
    for i, move in enumerate(keter_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            keter_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            keter_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = keter_move_list_numbers[0]
        elif move_x == 2:
            move = keter_move_list_numbers[1]
        elif move_x == 3:
            move = keter_move_list_numbers[2]
        elif move_x == 4:
            move = keter_move_list_numbers[3]
        elif move_x == 5:
            move = keter_move_list_numbers[4]
        elif move_x == 0:
            move = keter_move_list_numbers[5]
        elif move_x == 11:
            move = keter_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(keter_moves.keys())[0]
            damage = battle_character["Strength"] * battle_character["Mana"] / 7
            if keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (keter_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character    
        
        elif move == '2':
            move_choice = list(keter_moves.keys())[1]
            damage = 5000000
            if keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (keter_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character

        elif move == '3':
            move_choice = list(keter_moves.keys())[2]
            damage = battle_character["Strength"] * battle_character["Mana"] / 7
            if keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (keter_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character
        
        elif move == '4':
            move_choice = list(keter_moves.keys())[3]
            damage = None
            if battle_character["Buffs"].get("Will of the Crown") is not None:
                encounter_text("You already have the buff [Will of the Crown] active!")
                continue
            elif keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use [{move_choice}]! Choose a different move.")
                continue
            elif keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                apply_buff(battle_character, "Will of the Crown")
                return move_choice, damage, "buff", battle_character
            else:
                battle_character["Mana"] -= (keter_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                apply_buff(battle_character, "Will of the Crown")
                return move_choice, damage, "buff", battle_character

        elif move == '5':
            move_choice = list(keter_moves.keys())[4]
            damage = battle_character["Strength"] * battle_character["Mana"] * battle_character["Health"] / (abs(battle_character["Wisdom"] * battle_character["Defense"] - 1000) + 1)
            if keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif keter_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (keter_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character


eloki_moves = {"(Link 5) Eloki: Law of Zero (Single, 0 Mana) [1]": {"Usage": "Damage", "Formula": "Strength**Strength", "Cost": 0, "Description": "A powerful single-target attack that utilizes the user's mana."},
               "(Link 5) Eloki: Infinity's Transgression (AOE, 0 Mana) [2]": {"Usage": "Damage", "Formula": "Mana**Mana", "Cost": 0, "Description": "A devastating area-of-effect attack utilizing the user's mana."}}

def eloki_decision(eloki_move_list, battle_character):
    global character
    eloki_move_list_numbers = []
    for i, move in enumerate(eloki_move_list):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            eloki_move_list_numbers.append(move)
    for i, move in enumerate(regular_moves):
            move = (move.split("["))[1]
            move = move.replace("]", "").strip()
            eloki_move_list_numbers.append(move)

    while True:
        move_x = question_input("Select a move (#): ").strip().lower()
        if move_x == "b" or move_x == "back":
            return "back", None, None, battle_character
        elif move_x == "m" or move_x == "menu":
            battle_menu(battle_character)
            clear()
            return None, None, None, battle_character

        try:
            move_x = int(move_x)
        except ValueError:
            encounter_text("Invalid move selection.")
            input_to_continue()
            clear()
            return None, None, None, battle_character
        else:
            if move_x not in [0, 1, 2, 3, 4, 5, 11]:
                encounter_text("Invalid move selection.")
                input_to_continue()
                clear()
                return None, None, None, battle_character

        
        if move_x == 1:
            move = eloki_move_list_numbers[0]
        elif move_x == 2:
            move = eloki_move_list_numbers[1]
        elif move_x == 0:
            move = eloki_move_list_numbers[5]
        elif move_x == 11:
            move = eloki_move_list_numbers[6]
    
        if move == '0':
            move_choice = list(regular_moves.keys())[0]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Defense"] *= regular_moves[move_choice]["Formula"]["Defend"]
            return move_choice, damage, ["buff", "restore"], battle_character
        
        elif move == '11':
            move_choice = list(regular_moves.keys())[1]
            damage = None
            battle_character["Mana"] += regular_moves[move_choice]["Formula"]["Restore"]
            battle_character["Health"] += regular_moves[move_choice]["Formula"]["Heal"]
            return move_choice, damage, ["heal", "restore"], battle_character
        
        elif move == '1':
            move_choice = list(eloki_moves.keys())[0]
            damage = battle_character["Strength"] ** battle_character["Strength"]
            if eloki_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif eloki_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "single", battle_character
            else:
                battle_character["Mana"] -= (eloki_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "single", battle_character
        
        elif move == '2':
            move_choice = list(eloki_moves.keys())[1]
            damage = battle_character["Mana"] ** battle_character["Mana"]
            if eloki_moves[move_choice]["Cost"] - battle_character["Wisdom"] > battle_character["Mana"]:
                encounter_text(f"You don't have enough Mana to use {move_choice}! Choose a different move.")
                continue
            elif eloki_moves[move_choice]["Cost"] - battle_character["Wisdom"] < 0:
                return move_choice, damage, "aoe", battle_character
            else:
                battle_character["Mana"] -= (eloki_moves[move_choice]["Cost"] - battle_character["Wisdom"])
                return move_choice, damage, "aoe", battle_character












# Achievements system, will be run after a lot of other functions
def achievements():
    ...



# EVERYTHING RELATED TO TYPING EFFECTS AND INPUTS

#rpg text typing effect
def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
    print()

# for quick text display
def quick_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def custom_text(text, custom_time):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(custom_time)
    print()

# asking a question/decision
def question_input(text):
    quick_text(text)
    clear_last_line()
    answer = input(text)
    return answer

# input to continue
def input_to_continue():
    print("")
    i = question_input("Input any key to continue: ")
    print("")

#loading effect
def loading():
    clear()
    for _ in range(3):
        for i in range(3):
            print("Loading" + "." * (i + 1), end="\r")
            time.sleep(0.5)
            print(" " * 20, end="\r")
    clear()

# ... effect
def dot_effect(text):
    for _ in range(3):
        for i in range(3):
            print(f"{text}" + "." * (i + 1), end="\r")
            time.sleep(0.5)
            print(" " * (len(text) + 3), end="\r")


#monologue effect
def monologue(text):
    for line in text:
        type_text(line)
        time.sleep(0.33)

def quick_monologue(text):
    for line in text:
        quick_text(line)
        time.sleep(0.33)

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#encounter text typing effect
def encounter_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.035)
    print()

def gibtext(text, speed=0.02, lock_delay=0.02):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    current = [random.choice(chars) if c != " " else " " for c in text]
    locked = [False] * len(text)

    sys.stdout.write("".join(current))
    sys.stdout.flush()

    for i in range(len(text)):
        start = time.time()

        # scramble everything except locked characters
        while time.time() - start < lock_delay:
            for j in range(len(text)):
                if not locked[j] and text[j] != " ":
                    current[j] = random.choice(chars)

            sys.stdout.write("\r" + "".join(current))
            sys.stdout.flush()
            time.sleep(speed)

        # lock next character
        locked[i] = True
        current[i] = text[i]
        sys.stdout.write("\r" + "".join(current))
        sys.stdout.flush()

    print()



def encounter(enemy_name):
    x = random.choice([f"A ENEMY APPEARS!",
                      f"ENCOUNTER!",
                      f"You have stumbled upon an enemy!",
                      f"An enemy approaches!",
                      f"Genesis: Watch out! An enemy is nearby!",
                      f"Genesis: Scanning... Enemy detected ahead!",
                      f"Genesis: Warning! Hostile entities detected!",
                      f"Genesis: Alert! Potential threats in the vicinity!"])
    type_text(x)
    encounter_text(f"You encounter a {enemy_name}! ")
    input_to_continue()
    clear()


def boss_encounter(boss_name):
    enemy = bosses[boss_name]
    encounter_text(f"You face against {boss_name}! ")
    encounter_text(f"Genesis: Analyzing {boss_name} stats...")
    for stat, val in enemy.items():
        encounter_text(f" - {stat}: {val}")
    print(" ")

def death():
    clear()
    text = ["Genesis: You have perished...", 
            "Genesis: It's unfortunate, but such is the way of the world.",
            "Genesis: That's too bad.",
            "Genesis: I was hoping that you would have made it till the end...",
            "Genesis: But alas, it seems that fate had other plans for you.",
            "Genesis: It seems like that they have won once again.",
            "Genesis: Goodbye... Player."]
    monologue(text)
    time.sleep(2)
    loading()
    text = ("Game Over.",
            "Thank you for playing PENTA.",
            "Developed by James Jeong",
            "All rights reserved (I guess)",
            "'Deuteronomy 30:19:",
            "\"I have set before you life and death, blessing and curse; therefore choose life, that you and your descendants may live\"",
            "See you on your next playthrough...")
    monologue([text])
    i = question_input("Input any key to exit the game: ")
    exit()

def clear_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush()


def three_choices(texta, textb, textc):
    quick_text(f"A. {texta}")
    quick_text(f"B. {textb}")
    quick_text(f"C. {textc}")
    x = question_input(">>> ").strip().lower()
    clear_last_line()
    clear_last_line()
    clear_last_line()
    clear_last_line()
    return x

def rarity(chance, item):
    if chance >= 0.25:
                common = random.choice([f"COMMON FIND! You have obtained a {item}.", 
                          f"COMMON FIND! You pick up a {item}.",
                          f"COMMON FIND! You put a {item} into your inventory.",
                          f"COMMON FIND! The chest reveals a {item}.",
                          f"COMMON FIND! Inside the chest is a {item}."])
                encounter_text(common)
    elif 0.1 < chance < 0.25:
                uncommon = random.choice([f"UNCOMMON FIND! You have obtained a {item}.", 
                          f"UNCOMMON FIND! You pick up a {item}.",
                          f"UNCOMMON FIND! You put a {item} into your inventory.",
                          f"UNCOMMON FIND! The chest reveals a {item}.",
                          f"UNCOMMON FIND! Inside the chest is a {item}."])
                encounter_text(uncommon)
    elif 0.03 < chance <= 0.1:
                rare = random.choice([f"RARE FIND! You have obtained a {item}.", 
                          f"RARE FIND! You pick up a {item}.",
                          f"RARE FIND! You put a {item} into your inventory.",
                          f"RARE FIND! The chest reveals a {item}.",
                          f"RARE FIND! Inside the chest is a {item}."])
                encounter_text(rare)
    elif 0.01 < chance <= 0.03:
                epic = random.choice([f"EPIC FIND! You have obtained a {item}.", 
                          f"EPIC FIND! You pick up a {item}.",
                          f"EPIC FIND! You put a {item} into your inventory.",
                          f"EPIC FIND! The chest reveals a {item}.",
                          f"EPIC FIND! Inside the chest is a {item}."])
                encounter_text(epic)
    elif 0.001 < chance <= 0.01:
                legendary = random.choice([f"LEGENDARY FIND! You have obtained a {item}.", 
                          f"LEGENDARY FIND! You pick up a {item}.",
                          f"LEGENDARY FIND! You put a {item} into your inventory.",
                          f"LEGENDARY FIND! The chest reveals a {item}.",
                          f"LEGENDARY FIND! Inside the chest is a {item}."])
                encounter_text(legendary)
    elif 0.0005 < chance <= 0.001:
                mythic = random.choice([f"MYTHIC FIND! You have obtained a {item}.", 
                          f"MYTHIC FIND! You pick up a {item}.",
                          f"MYTHIC FIND! You put a {item} into your inventory.",
                          f"MYTHIC FIND! The chest reveals a {item}.",
                          f"MYTHIC FIND! Inside the chest is a {item}."])
                encounter_text(mythic)
    elif 0.00005 < chance <= 0.0005:
                divine = random.choice([f"DIVINE FIND! You have obtained a {item}.", 
                          f"DIVINE FIND! You pick up a {item}.",
                          f"DIVINE FIND! You put a {item} into your inventory.",
                          f"DIVINE FIND! The chest reveals a {item}.",
                          f"DIVINE FIND! Inside the chest is a {item}."])
                encounter_text(divine)
    else:
                special = random.choice([f"SPECIAL FIND! You have obtained a {item}.", 
                          f"SPECIAL FIND! You pick up a {item}.",
                          f"SPECIAL FIND! You put a {item} into your inventory.",
                          f"SPECIAL FIND! The chest reveals a {item}.",
                          f"SPECIAL FIND! Inside the chest is a {item}."])
                encounter_text(special)

def battle_menu(battle_character):
    switch = True
    while True:
        clear()
        if switch:
            quick_text("╔═══════ PLAYER MENU (CURRENTLY IN BATTLE) ═══════╗")
            x = question_input("Stats (s), Inventory (i, disabled), Craft (c, disabled), PAU (p, disabled), Location(l), Back (b), Quit (q): ").strip().lower()
        if not switch:
            print("╔═══════ PLAYER MENU (CURRENTLY IN BATTLE) ═══════╗")
            x = input("Stats (s), Inventory (i, disabled), Craft (c, disabled), PAU (p, disabled), Location(l), Back (b), Quit (q): ").strip().lower()
        
        clear()
        if x == 's':
            for stat, current_value in battle_character.items():
                if stat in ["Strength", "Defense", "Health", "Mana", "Mana Regen", "Wisdom", "Luck", "Dodge", "Parry", "Critical", "Stat Inheritance"]:
                    encounter_text(f"{stat}: {current_value} / {character[stat]}")
            x = question_input("Input any key to go back to the menu: ").strip().lower()
            switch = False
            continue
        elif x == 'i':
            encounter_text("You cannot access your inventory during battle!")
            x = question_input("Input any key to go back to the menu: ").strip().lower()
            switch = False
            continue
        elif x == "c":
            encounter_text("You cannot craft during battle!")
            x = question_input("Input any key to go back to the menu: ").strip().lower()
            switch = False
            continue
        elif x == "p":
            encounter_text("You cannot do that during battle!")
            x = question_input("Input any key to go back to the menu: ").strip().lower()
            switch = False
            continue
        elif x == "l":
            clear()
            type_text(f"Current Location: {character['Location']}")
            type_text(f"Current Coordinate: {character['Coordinate']}")
            input_to_continue()
            switch = False
            continue
        elif x == 'b':
             return None
        elif x == 'q':
            encounter_text("You cannot quit the game during battle!")
            x = question_input("Input any key to go back to the menu: ").strip().lower()
        else:
            quick_text("Invalid option.")
            input_to_continue()
            continue

def rarity_sort(some_list):
    list_of_items = []
    some_list.sort()
    rarity_order = ["{BROKEN}", "{DAMAGED}", "{UNFINISHED}", "{Common}", "{Uncommon}", "{Rare}", "{Epic}", "{Legendary}", "{Mythic}", "{Divine}", "{Special}"]
    for rarity in rarity_order:
        for thing in some_list:
            if thing.split(" ")[-1] == rarity:
                list_of_items.append(thing)
    return list_of_items



