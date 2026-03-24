import time
import random
import sys
import os
import json
from PENTAutilities import character
from PENTAutilities import type_text, encounter_text, quick_text, question_input, input_to_continue, clear
from PENTAutilities import rarity_sort
from PENTAlore import lore


# Lore
books = {"'Houlester's Guide to the 10 Sefirots' {DAMAGED}": {"Description": "A damaged book that explains pretty much everything to do about the Sefirots."},
         "'Jess' Journal' {DAMAGED}": {"Description": "A damaged journal that contains the thoughts and experiences of a person named Jess."}}

# Loot
chest_count = []
book_count = []


weapons = {"'Shiny Sword' {Rare}": {"Description": "A useless sword that offers no benefits but it's aesthetic appeal.",
                                    "Craft": ["Uncraftable"]},
           "'Shiny Sword Alpha' {Epic}": {"Strength": +100, "Mana": +100, "Description": "A sword that offers more benefits than just its aesthetic appeal.",
                                    "Craft": ["Uncraftable"]},
           "'Saebr' {Rare}": {},
           "'Stick' {Common}": {"Strength": +5, "Description": "A regular stick.",
                                "Craft": ["Uncraftable"]},
           "'Magic Stick' {Rare}": {"Mana": +100, "Description": "A not-so-regular stick infused with mana.",
                                    "Craft": ["Uncraftable"]},
           "'Stone Dagger' {Common}": {"Strength": +5, "Mana": +5, "Health": +5, "Description": "A small but sharp dagger made of stone.",
                                       "Craft": ["'Stick' {Common}", "'Stone' {Common}"]},
           "'Stone Sword' {Common}": {"Strength": +15, "Description": "A makeshift sword made of stone.",
                                      "Craft": ["'Stick' {Common}", "'Stone' {Common}", "'Stone' {Common}"]},
           "'Stone Spear' {Common}": {"Strength": +5, "Health": +10, "Description": "A long makeshift spear made of stone.",
                                      "Craft": ["'Stick' {Common}", "'Stick' {Common}", "'Stone' {Common}"]},
           "'Stone Hammer' {Common}": {"Strength": +10, "Health": +10, "Mana": -5, "Description": "A makeshift hammer made of stone.",
                                       "Craft": ["'Stick' {Common}", "'Stone' {Common}", "'Scrap' {Common}"]},
           "'Stone Shield' {Common}": {"Strength": -5, "Health": + 10, "Defense": +10, "Description": "A huge rock carved to the form of a shield.",
                                       "Craft": ["'Stone' {Common}", "'Scrap' {Common}"]},
           "'Iron Dagger' {Uncommon}": {"Strength": +10, "Mana": +10, "Health": +5, "Description": "A small but sharp dagger made of iron.",
                                        "Craft": ["'Stick' {Common}", "'Iron' {Uncommon}"]},
           "'Iron Sword' {Uncommon}": {"Strength": +20, "Health": +5, "Description": "A forged sword made of iron.",
                                       "Craft": ["'Stick' {Common}", "'Iron' {Uncommon}", "'Iron' {Uncommon}"]},
           "'Iron Spear' {Uncommon}": {"Strength": +10, "Health": +15, "Description": "A long forged spear made of iron.",
                                       "Craft": ["'Stick' {Common}", "'Stick' {Common}", "'Iron' {Uncommon}"]},
           "'Iron Hammer' {Uncommon}": {"Strength": +20, "Health": +20, "Mana": -15, "Description": "A forged hammer made of iron.",
                                        "Craft": ["'Stick' {Common}", "'Iron' {Uncommon}", "'Scrap' {Common}"]},
           "'Iron Shield' {Uncommon}": {"Strength": +5, "Health": +10, "Mana": -15, "Defense": +25, "Description": "A mighty shield forged out of iron.",
                                        "Craft": ["'Iron' {Uncommon}", "'Scrap' {Common}"]},
           "'Gun' {Legendary}": {"Strength": +2005, "Description": "A frickin gun.",
                                 "Craft": ["Uncraftable"]},
           "'Drainer Scythe' {Legendary}": {"Strength": +500, "Health": -200, "Mana": +1000, "Description": "A scythe made of a worthy adventurer's bones. Imbued with a lifesteal effect.",
                                            "Craft": ["Uncraftable"]},
           "'Eel-Shark Ball": {},
           "'Light Blade' {}": {},
           "'Tennis Racket' {Common}": {}
                                        
}


armor = {"'Leather Armor' {Common}": {"Defense": +10, "Health": +10, "Description": "Armor made from toughened leather.",
                                      "Craft": ["'Leather' {Common}", "'Leather' {Common}", "'Leather' {Common}"]},
         "'Moss Armor' {Common}": {"Defense": +5, "Description": "Horrible armor made of moss.",
                                   "Craft": ["'Moss' {Common}", "'Moss' {Common}", "'Moss' {Common}"]},
         "'Scrap Armor' {Common}": {"Defense": +7, "Description": "Horrible armor made up of random metal objects.",
                                    "Craft": ["'Scrap' {Common}", "'Scrap' {Common}", "'Scrap' {Common}"]},
         "'Iron Armor' {Uncommon}": {"Defense": +40, "Health": +20, "Description": "Sturdy armor forged from iron.",
                                     "Craft": ["'Iron' {Uncommon}", "'Iron' {Uncommon}", "'Iron' {Uncommon}"]}}



items = {"'Health Potion' {Common}": {"Heal": 100, "Description": "A potion that heals 100 health.",
                                      "Craft": ["Uncraftable"]},
         "'Mana Potion' {Common}": {"Restore": 100, "Description": "A potion that restores 100 mana.",
                                    "Craft": ["Uncraftable"]},
        "'Forest Key' {Epic}": {"Description": "A key that unveils the secrets of the Starting Forest.",
                                "Craft": ["'Stick' {Common}", "'Moss' {Common}",  "'Scrap' {Common}"]},
        "'Rejamesinator' {Rare}": {"Heal": 2500, "Description": "A bean with powerful healing powers.",
                                   "Craft": ["Uncraftable"]}
                                
                                    }


all_items = weapons | armor | items

drops = {"'Stick' {Common}": {"Description": "A regular stick."},
         "'Moss' {Common}": {"Description": "A flowerless plant that can be used to craft armor."},
         "'Scrap' {Common}": {"Description": "A variety of useless metallic items formed into a ball-like shape."},
         "'Leather' {Common}": {"Description": "A somewhat durable and flexible material."},
         "'Iron' {Uncommon}": {"Description": "A smelted material that can be used in a variety of ways."},
         "'Stone' {Common}": {"Description": "A rock."},
         "'Mana Dust' {Epic}": {"Description": "A physical manifestation of mana in a powdery-like form."},
         "'Mana Essence' {Legendary}": {"Description": "A physical manifestation of mana in a sphere-like form."},
         "'Flower Core' {Legendary}": {"Description": "A physical manifestation of a creature's connection to nature."},
         "'Steel Core' {Legendary}": {"Description": "A physical manifestation of a creature's connection to the underground."},
         "'Mana Core' {Mythic}": {"Description": "A physical manifestation of a creature's connection to mana."}}



#add op stuff but super rare chance
enemy_loot_tables = {"Mossling": {"Loot": ["'Stick' {Common}", "'Moss' {Common}", "'Moss' {Common}", "'Scrap' {Common}", "'Leather' {Common}", "'Iron' {Uncommon}", "'Flower Core' {Legendary}"], 
                                  "Chance": [50, 50, 25, 25, 25, 15, 1]},
                     "Pebblekin": {"Loot": ["'Stick' {Common}", "'Stone' {Common}", "'Scrap' {Common}", "'Iron' {Uncommon}", "'Steel Core' {Legendary}"], 
                                   "Chance": [50, 50, 25, 20, 1]},
                     "Forest Wisp": {"Loot": ["'Moss' {Common}", "'Magic Stick' {Rare}", "'Mana Dust' {Epic}", "'Mana Essence' {Legendary}'", "'Mana Core' {Mythic}"], 
                                     "Chance": [50, 5, 3, 1, 0.1]},
                     "Rock Golem": {"Loot": ["'Scrap' {Common}", "'Iron' {Uncommon}", "'Iron' {Uncommon}", "'Mana Essence' {Legendary}", "'Steel Core' {Legendary}"],
                                   "Chance": [100, 75, 50, 2, 2]}
                                     
}


def get_loot(enemy):
    temp_list = []
    for loot in range(len(enemy_loot_tables[enemy]["Loot"])):
        chance = enemy_loot_tables[enemy]["Chance"][loot] / (100 - character["Luck"] * 0.5)
        roll = random.random()
        if roll <= chance:
            character["Inventory"].append(enemy_loot_tables[enemy]["Loot"][loot])
            temp_list.append(enemy_loot_tables[enemy]["Loot"][loot])
            if chance >= 0.25:
                common = random.choice([f"COMMON DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
                          f"COMMON DROP! You pick up a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"COMMON DROP! You put a {enemy_loot_tables[enemy]["Loot"][loot]} into your inventory.",
                          f"COMMON DROP! {enemy} has dropped a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"COMMON DROP! The {enemy} drops a {enemy_loot_tables[enemy]["Loot"][loot]}."])
                encounter_text(common)
            elif 0.1 < chance < 0.25:
                uncommon = random.choice([f"UNCOMMON DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
                          f"UNCOMMON DROP! You pick up a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"UNCOMMON DROP! You put a {enemy_loot_tables[enemy]["Loot"][loot]} into your inventory.",
                          f"UNCOMMON DROP! {enemy} has dropped a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"UNCOMMON DROP! The {enemy} drops a {enemy_loot_tables[enemy]["Loot"][loot]}."])
                encounter_text(uncommon)
            elif 0.03 < chance <= 0.1:
                rare = random.choice([f"RARE DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
                          f"RARE DROP! You pick up a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"RARE DROP! You put a {enemy_loot_tables[enemy]["Loot"][loot]} into your inventory.",
                          f"RARE DROP! {enemy} has dropped a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"RARE DROP! The {enemy} drops a {enemy_loot_tables[enemy]["Loot"][loot]}."])
                encounter_text(rare)
            elif 0.01 < chance <= 0.03:
                epic = random.choice([f"EPIC DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
                          f"EPIC DROP! You pick up a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"EPIC DROP! You put a {enemy_loot_tables[enemy]["Loot"][loot]} into your inventory.",
                          f"EPIC DROP! {enemy} has dropped a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"EPIC DROP! The {enemy} drops a {enemy_loot_tables[enemy]["Loot"][loot]}."])
                encounter_text(epic)
            elif 0.001 < chance <= 0.01:
                legendary = (random.choice[f"LEGENDARY DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
                          f"LEGENDARY DROP! You pick up a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"LEGENDARY DROP! You put a {enemy_loot_tables[enemy]["Loot"][loot]} into your inventory.",
                          f"LEGENDARY DROP! {enemy} has dropped a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"LEGENDARY DROP! The {enemy} drops a {enemy_loot_tables[enemy]["Loot"][loot]}."])
                encounter_text(legendary)
            elif 0.0005 < chance <= 0.001:
                mythic = random.choice([f"MYTHIC DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
                          f"MYTHIC DROP! You pick up a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"MYTHIC DROP! You put a {enemy_loot_tables[enemy]["Loot"][loot]} into your inventory.",
                          f"MYTHIC DROP! {enemy} has dropped a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"MYTHIC DROP! The {enemy} drops a {enemy_loot_tables[enemy]["Loot"][loot]}."])
                encounter_text(mythic)
            elif 0.00005 < chance <= 0.0005:
                divine = random.choice([f"DIVINE DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
                          f"DIVINE DROP! You pick up a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"DIVINE DROP! You put a {enemy_loot_tables[enemy]["Loot"][loot]} into your inventory.",
                          f"DIVINE DROP! {enemy} has dropped a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"DIVINE DROP! The {enemy} drops a {enemy_loot_tables[enemy]["Loot"][loot]}."])
                encounter_text(divine)
            elif chance <= 0.00005:
                special = random.choice([f"SPECIAL DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
                          f"SPECIAL DROP! You pick up a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"SPECIAL DROP! You put a {enemy_loot_tables[enemy]["Loot"][loot]} into your inventory.",
                          f"SPECIAL DROP! {enemy} has dropped a {enemy_loot_tables[enemy]["Loot"][loot]}.",
                          f"SPECIAL DROP! The {enemy} drops a {enemy_loot_tables[enemy]["Loot"][loot]}."])
                encounter_text(special)
    if len(temp_list) == 0:
            nothing = random.choice([f"{enemy} didn't drop any loot!",
                                    f"Unluckly! No loot.",
                                    f"The {enemy} dropped nothing.",
                                    f"{enemy} was broke.",
                                    f"{enemy} dropped nothing.",
                                    f"No loot was dropped."])
            encounter_text(nothing)
        
    character["Inventory"].sort()


def craft():
    global character
    list_of_items = []
    crafting_circle = []
    clear()
    quick_text("A circle of space-like void fades into your vision in front of you.")
    input_to_continue()
    clear()
    

    while True:
        character["Inventory"] = rarity_sort(character["Inventory"])
        clear()
        list_of_items = []
        quick_text("Materials:")
        for i, item_in_inventory in enumerate(character["Inventory"]):
            quick_text(f"{i + 1}. {item_in_inventory}")
            list_of_items.append(item_in_inventory)
        if len(character["Inventory"]) == 0:
            quick_text("No Materials Left")

        materials = question_input("Input material (#), Remove material (r), Initiate Craft (c), reveal Inventory (i), Quit (q): ").strip()
        if materials == "q" or materials == "Q":
            return None
        
        elif materials == "r" or materials == "R":
            quick_text("Materials Currently in Crafting Void:")
            for i, crafting_materials in enumerate(crafting_circle):
                quick_text(f"{i + 1}. {crafting_materials}")
                while True:
                    item_to_remove = question_input("Remove material (#), Back (b): ").lower().strip()
                    if item_to_remove == "b" or item_to_remove == "B":
                        continue

                    try:
                        item_to_remove = int(item_to_remove)
                    except ValueError:
                        quick_text("Input a valid number.")
                        input_to_continue()
                        continue
                    else:
                        if item_to_remove > len(crafting_circle) or item_to_remove <= 0:
                            quick_text("Input a valid number.")
                            input_to_continue()
                            continue
 
                    character["Inventory"].append(crafting_circle[item_to_remove - 1])
                    crafting_circle.remove(crafting_circle[item_to_remove - 1])


        elif materials == "c" or materials == "C":
            clear()
            for recipe in all_items.keys():
                if crafting_circle.sort() == all_items[recipe]["Craft"].sort() and len(crafting_circle) == len(all_items[recipe]["Craft"]):
                    character["Inventory"].append(recipe)
                    x = random.choice([f"{recipe.split()[-1]} CRAFT! You have created a {recipe}.",
                                      f"{recipe.split()[-1]} CRAFT! You have successfully made a {recipe}.",
                                      f"{recipe.split()[-1]} CRAFT! You have made a {recipe}.",
                                      f"{recipe.split()[-1]} CRAFT! You have crafted a {recipe}.",
                                      f"{recipe.split()[-1]} CRAFT! The crafting void reveals a {recipe}.",
                                      f"{recipe.split()[-1]} CRAFT! A {recipe} floats out of the crafting void",
                                      f"{recipe.split()[-1]} CRAFT! A {recipe} has been created."])
                    quick_text(x)
                    input_to_continue()
                    clear()
                    some_random_variable = "yes"
                    break
            if some_random_variable == "yes":
                continue
            else:    
                character["Inventory"].append(crafting_circle)
                x = random.choice(["The crafting circle spews back the inserted materials back at you",
                                        "Nothing was crafted.",
                                        "The crafting circle reveals no item",
                                        "Your attempt at crafting has failed",
                                        "Better luck next time. Nothing was created.",
                                        "NO CRAFT!",
                                        "Crafting attempt unsuccessful.",
                                        "Crafting was unsuccessful."])
                quick_text(x)
                input_to_continue()
                clear()
                continue
            
        
        elif materials == "i" or materials == "I":
            list_of_items = []
            for i, item_in_inventory in enumerate(character["Inventory"]):
                quick_text(f"{i + 1}. {item_in_inventory}")
                list_of_items.append(f"{i + 1}. {item_in_inventory}")
                continue
        

        try:
            materials = int(materials)
        except ValueError:
            quick_text("Input a valid number.")
            input_to_continue()
            continue
        else:
            if materials > len(list_of_items) or materials <= 0:
                quick_text("Input a valid number.")
                input_to_continue()
                continue


            crafting_circle.append(list_of_items[materials - 1])
            character["Inventory"].remove(list_of_items[materials - 1])
            list_of_items.remove(list_of_items[materials - 1])


def allocate(attribute):
    global character
    while True:
        quick_text(f"You have {character[attribute]} units in {attribute}.")
        quick_text(f"You have {character["POTENTIAL"]} POTENTIAL.")
        quick_text("Invest POTENTIAL (#), Back (b)")
        decision_s = question_input(">>> ")
        if decision_s == "b" or decision_s == "back" or decision_s == "B" or decision_s == "Back":
            break
        try:
            decision_s = int(decision_s)
        except ValueError:
            quick_text("Invalid input.")
            input_to_continue()
            continue
        else:
            if character["POTENTIAL"] < decision_s:
                quick_text("You don't have that many POTENTIAL!")
                input_to_continue()
                continue
            else:
                character["POTENTIAL"] -= decision_s
                character[attribute] += decision_s
                quick_text(f"You have allocated {decision_s} PAUs into your {attribute} attribute.")
                input_to_continue()
                clear()
                break

def create(attribute):
     global character
     while True:
        quick_text(f"You have {character[attribute]} units in {attribute}.")
        quick_text(f"You have {character["POTENTIAL"]} POTENTIAL.")
        quick_text("Create POTENTIAL (#), Back (b)")
        decision_s = question_input(">>> ")
        if decision_s == "b" or decision_s == "back" or decision_s == "B" or decision_s == "Back":
            break
        try:
            decision_s = int(decision_s)
        except ValueError:
            quick_text("Invalid input.")
            input_to_continue()
            continue
        else:
            if character[attribute] < decision_s:
                quick_text("You don't have that many stat units!")
                input_to_continue()
                continue
            elif character[attribute] == decision_s:
                quick_text("That is not possible.")
                input_to_continue()
                continue
            else:
                character["POTENTIAL"] += decision_s
                character[attribute] -= decision_s
                quick_text(f"You have withthrew {decision_s} PAUs from your {attribute} attribute.")
                input_to_continue()
                clear()
                break


def potential():
    global character
    stat_list = ["Strength", "Defense", "Health", "Mana"]
    while True:
        clear()
        decision = question_input("Allocate POTENTIAL (a), Create POTENTIAL (c), Back (b): ").strip().lower()
        if decision == "b" or decision == "back" or decision == "B" or decision == "Back":
            break
        elif decision == "a":
            clear()
            quick_text("Possible stats to use POTENTIAL on:")
            for attribute in stat_list:
                quick_text(f"{attribute}: {character[attribute]}")
            quick_text("Strength (s), Defense (d), Health (h), Mana (m): ")
            decision_1 = question_input(">>> ").strip().lower()
            clear()

            if decision_1 == "s":
                allocate("Strength")
            elif decision_1 == "d":
                allocate("Defense")
            elif decision_1 == "h":
                allocate("Health")
            elif decision_1 == "m":
                allocate("Mana")

        elif decision == "c":
            clear()
            quick_text("Possible stats to draw POTENTIAL from:")
            for attribute in stat_list:
                quick_text(f"{attribute}: {character[attribute]}")
            quick_text("Strength (s), Defense (d), Health (h), Mana (m): ")
            decision_1 = question_input(">>> ").strip().lower()
            clear()

            if decision_1 == "s":
                create("Strength")
            elif decision_1 == "d":
                create("Defense")
            elif decision_1 == "h":
                create("Health")
            elif decision_1 == "m":
                create("Mana")
        

        else:
            quick_text("Invalid input.")
            input_to_continue()
            continue

def use(item):
    type_text("Nothing happened.")
    input_to_continue()
    clear()
    

#the main menu of the game
def menu():
    switch = True
    while True:
        clear()
        if switch:
            quick_text("╔══════════════════ PLAYER MENU ══════════════════╗")
            x = question_input("Stats (s), Inventory (i), Craft (c), PAU (p), Location(l), Back (b), Quit (q): ").strip().lower()
        if not switch:
            print("╔══════════════════ PLAYER MENU ══════════════════╗")
            x = input("Stats (s), Inventory (i), Craft (c), PAU (p), Location(l), Back (b), Quit (q): ").strip().lower()
        if x == 's':
            menu_stats()
            switch = False
            continue
        elif x == 'i':
            inventory()
            switch = False
            continue
        elif x == "c":
            craft()
            switch = False
            continue
        elif x == "p":
            potential()
            switch = False
            continue
        elif x == "l":
            clear()
            switch = False
            type_text(f"Current Location: {character['Location']}")
            type_text(f"Current Coordinate: {character['Coordinate']}")
            input_to_continue()
            continue
        elif x == 'b':
            switch = False
            clear()
            break
        elif x == "q":
            clear()
            switch = False
            save_game()
            sys.exit()
            
        else:
            print("Invalid option.")
            switch = False
            input_to_continue()
            continue



def menu_stats():
    clear()
    quick_text("╔═════════ PLAYER STATS ═════════╗")
    stat_lists = ["Strength", "Defense", "Health", "Mana", "Mana Regen", "Wisdom", "Luck", "Dodge", "Parry", "Critical", "Stat Inheritance"]
    for stat in stat_lists:
        quick_text(f"{stat} - {character[stat]}")
    print("")
    x = question_input("Input any key to go back to the menu: ").strip().lower()
    clear()


    
# FINISH THIS
def inventory():
    global character
    craft_description_list = ["Craft", "Description"]
    while True:
        clear()
        list_of_items = []
        rarity_order = ["{BROKEN}", "{DAMAGED}", "{UNFINISHED}", "{Common}", "{Uncommon}", "{Rare}", "{Epic}", "{Legendary}", "{Mythic}", "{Divine}", "{Special}"]
        x = 1
        quick_text("╔═════════ PLAYER INVENTORY ═════════╗")
        if len(character['Inventory']) == 0:
            type_text("You have no items in your inventory.")
            print("")

        for rarity in rarity_order:
            for item_in_inventory in character["Inventory"]:
                    if item_in_inventory.split(" ")[-1] == rarity:
                        list_of_items.append(item_in_inventory)
                        quick_text(f"{x}. {item_in_inventory}")
                        x += 1
        
        x = question_input("Use Item in Inventory (#), Current Equipment (e), Back (b): ").strip().lower()
        clear()
        try:
            x = int(x)
        except ValueError:
            if x == "e":
                    clear()
                    quick_text("╔═════════ Held Weapon/Armor ═════════╗")
                    quick_text(f"Held Weapon: {character['Held_Weapon']}")
                    quick_text(f"Held Armor: {character['Held_Armor']}")
                    print("")
                    if character["Held_Weapon"] == None and character["Held_Armor"] == None:
                        input_to_continue()
                        continue
                    elif character["Held_Weapon"] == None and character["Held_Armor"] != None:
                        x = question_input("Take off armor (b), Back (anything else): ").strip().lower()
                        if x == "b":
                            clear()
                            for armor_stat in armor[character["Held_Armor"]].keys():
                                if armor_stat not in craft_description_list:
                                    character[armor_stat] -= armor[character["Held_Armor"]][armor_stat]
                            character["Inventory"].append(character['Held_Armor'])
                            quick_text(f"You have taken off the {character["Held_Armor"]}.")
                            character['Held_Armor'] = None
                        else:
                            continue
                        input_to_continue()
                        continue
                    elif character["Held_Weapon"] != None and character["Held_Armor"] == None:
                        x = question_input("Take off weapon (a), Back (anything else): ").strip().lower()
                        if x == "a":
                            clear()
                            for weapon_stat in weapons[character["Held_Weapon"]].keys():
                                if weapon_stat not in craft_description_list:
                                    character[weapon_stat] -= weapons[character["Held_Weapon"]][weapon_stat]
                            character["Inventory"].append(character["Held_Weapon"])
                            quick_text(f"You have taken off the {character["Held_Weapon"]}.")
                            character['Held_Weapon'] = None
                        else:
                            continue
                        input_to_continue()
                        continue
                    elif character["Held_Weapon"] != None and character["Held_Armor"] != None:
                        x = question_input("Take off weapon (a), Take off armor (b), Back (anything else): ").strip().lower()
                        if x == "a":
                            clear()
                            for weapon_stat in weapons[character["Held_Weapon"]].keys():
                                if weapon_stat not in craft_description_list:
                                    character[weapon_stat] -= weapons[character["Held_Weapon"]][weapon_stat]
                            character["Inventory"].append(character["Held_Weapon"])
                            quick_text(f"You have taken off the {character["Held_Weapon"]}.")
                            character['Held_Weapon'] = None
                        elif x == "b":
                            clear()
                            for armor_stat in armor[character["Held_Armor"]].keys():
                                if armor_stat not in craft_description_list:
                                    character[armor_stat] -= armor[character["Held_Armor"]][armor_stat]
                            character["Inventory"].append(character['Held_Armor'])
                            quick_text(f"You have taken off the {character["Held_Armor"]}.")
                            character['Held_Armor'] = None
                        else:
                            continue
                        input_to_continue()
                        continue
            elif x == "b":
                return None
            else:
                quick_text("Invalid input.")
                input_to_continue()
                continue

        else:
            x -= 1
            if list_of_items[x] in weapons.keys():
                quick_text(f"You have summoned the {list_of_items[x]} out of your inventory.")
                time.sleep(0.5)
                decision = question_input(f"Equip (e), Drop (d), Info (i), Back (b): ").strip().lower()
                if decision == 'e':
                    clear()
                    if character["Held_Weapon"] == None:
                        pass

                    else:
                        for weapon_stat in weapons[character["Held_Weapon"]].items():
                            if weapon_stat not in craft_description_list:
                                character[weapon_stat] -= weapons[character["Held_Weapon"]][weapon_stat]

                    for weapon_stat in weapons[list_of_items[x]]:
                        if weapon_stat not in craft_description_list:
                                character[weapon_stat] += weapons[list_of_items[x]][weapon_stat]
                    
                    character["Inventory"].remove(list_of_items[x])
                    if character["Held_Weapon"] == None:
                        pass
                    else:
                        character["Inventory"].append(character["Held_Weapon"])
                    
                    character["Held_Weapon"] = list_of_items[x]
                    type_text(f"You have equipped a {list_of_items[x]}.")
                    input_to_continue()
                    continue


                elif decision == 'd':
                    clear()
                    type_text(f"You dropped a {list_of_items[x]}.")
                    character["Inventory"].remove(list_of_items[x])
                    input_to_continue()
                    continue
                elif decision == 'i':
                    clear()
                    quick_text(f"╔═════════ {list_of_items[x]} ═════════╗")
                    for stat, val in weapons[list_of_items[x]].items():
                        if stat == "Craft":
                            pass
                        else:
                            type_text(f" - {stat}: {val}")
                    input_to_continue()
                    continue
                elif decision == 'b':
                    continue
                else:
                    clear()
                    type_text("Invalid option.")
                    input_to_continue()
                    continue
            

            elif list_of_items[x] in armor.keys():
                quick_text(f"You have summoned a {list_of_items[x]} out of your inventory.")
                time.sleep(0.5)
                decision = question_input(f"{list_of_items[x]}: Equip (e), Drop (d), Info (i), Back (b): ").strip().lower()
                if decision == 'e':
                    clear()
                    if character["Held_Armor"] == None:
                        pass

                    else:
                        for armor_stat in armor[character["Held_Armor"]].items():
                            if armor_stat not in craft_description_list:
                                character[armor_stat] -= armor[character["Held_Armor"]][armor_stat]


                    for armor_stat in armor[list_of_items[x]]:
                        if armor_stat not in craft_description_list:
                            character[armor_stat] += armor[list_of_items[x]][armor_stat] 
                     
                    character["Inventory"].remove(list_of_items[x])
                    if character["Held_Armor"] == None:
                        pass
                    else:
                        character["Inventory"].append(character["Held_Armor"])
                    character["Held_Armor"] = list_of_items[x]
                    type_text(f"You have equipped the {list_of_items[x]}.")
                    input_to_continue()
                    continue

                elif decision == 'd':
                    clear()
                    type_text(f"You dropped a {list_of_items[x]}.")
                    character["Inventory"].remove(list_of_items[x])
                    input_to_continue()
                    continue
                elif decision == 'i':
                    clear()
                    quick_text(f"╔═════════ {list_of_items[x]} ═════════╗")
                    for stat, val in weapons[list_of_items[x]].items():
                        if stat == "Craft":
                            pass
                        else:
                            type_text(f" - {stat}: {val}")
                    input_to_continue()
                    continue
                    continue
                elif decision == 'b':
                    continue
                else:
                    clear()
                    type_text("Invalid option.")
                    input_to_continue()
                    continue

            
            elif list_of_items[x] in items.keys():
                quick_text(f"You have summoned the {x} out of your inventory.")
                time.sleep(0.5)
                decision = question_input(f"{x}: Use (u), Drop (d), Info (i) Back (b): ").strip().lower()
                if decision == 'u':
                    clear()
                    character["Inventory"].remove(x)
                    type_text(f"You used a {x}.")
                    use(x)
                    input_to_continue()
                    continue
                elif decision == 'd':
                    clear()
                    type_text(f"You dropped a {x}.")
                    character["Inventory"].remove(x)
                    input_to_continue()
                    continue
                elif decision == 'i':
                    clear()
                    quick_text(f"╔═════════ {list_of_items[x]} ═════════╗")
                    quick_text(f"{items[list_of_items[x]]['Description']}")
                    input_to_continue()
                    continue
                elif decision == 'b':
                    continue
                else:
                    clear()
                    type_text("Invalid option.")
                    input_to_continue()
                    continue
            
            elif list_of_items[x] in drops.keys():
                clear()
                quick_text(f"You have summoned the {list_of_items[x]} out of your inventory.")
                time.sleep(0.5)
                decision = question_input(f"{list_of_items[x]}: Drop (d), Info (i) Back (b): ").strip().lower()
                if decision == 'd':
                    clear()
                    type_text(f"You dropped a {list_of_items[x]}.")
                    character["Inventory"].remove(list_of_items[x])
                    input_to_continue()
                    continue
                elif decision == 'i':
                    clear()
                    quick_text(f"╔═════════ {list_of_items[x]} ═════════╗")
                    quick_text(f"{drops[list_of_items[x]]["Description"]}")
                    input_to_continue()
                    continue
                elif decision == 'b':
                    continue
                else:
                    clear()
                    type_text("Invalid option.")
                    input_to_continue()
                    continue
            
            elif list_of_items[x] in books.keys():
                quick_text(f"You have summoned the {list_of_items[x]} out of your inventory.")
                time.sleep(0.5)
                decision = question_input(f"{list_of_items[x]}: Read (r), Drop (d), Info (i) Back (b): ").strip().lower()
                if decision == 'r':
                    clear()
                    lore(list_of_items[x])
                    input_to_continue()
                    continue
                elif decision == 'd':
                    clear()
                    type_text(f"You dropped a {list_of_items[x]}.")
                    character["Inventory"].remove(list_of_items[x])
                    input_to_continue()
                    continue
                elif decision == 'i':
                    clear()
                    type_text(f"{list_of_items[x]} Info: ")
                    quick_text(f"╔═════════ {list_of_items[x]} ═════════╗")
                    quick_text(f"{books[list_of_items[x]]["Description"]}")
                    input_to_continue()
                    continue
                elif decision == 'b':
                    continue
                else:
                    type_text("Invalid option.")
                    input_to_continue()
                    continue



def save_game():
    global character
    clear()
    with open("save_file.json", "w") as file:
        json.dump(character, file, indent=4)

    quick_text("╔════════════ SAVE COMPLETE ════════════╗")
    quick_text("║ Progress has been recorded.           ║")
    quick_text("╚═══════════════════════════════════════╝")
    print("")
    input_to_continue()
    clear()


def load_game():
    global character
    clear()
    try:
        with open("save_file.json", "r") as file:
            character = json.load(file)

        quick_text("Save loaded successfully.")
        input_to_continue()
        clear()

    except FileNotFoundError:
        quick_text("No save file found. Starting new game.")
        input_to_continue()
        clear()




def delete_save():
    clear()
    if os.path.exists("save_file.json"):
        os.remove("save_file.json")
        quick_text("╔════════════ SAVE DELETED ════════════╗")
        quick_text("║ Progress has been erased.            ║")
        quick_text("╚══════════════════════════════════════╝")
        input_to_continue()
        clear()

    else:
        quick_text("╔══════════════ NO SAVE FOUND ═══════════════╗")
        quick_text("║ There is no save file to delete.           ║")
        quick_text("╚════════════════════════════════════════════╝")
        input_to_continue()
        clear()
    
