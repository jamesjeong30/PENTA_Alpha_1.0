import time
import random
import sys
import os
import json
from collections import Counter
from PENTAutilities import character, monologue
from PENTAutilities import type_text, encounter_text, quick_text, question_input, input_to_continue, clear, input_to_clear
from PENTAutilities import rarity_sort, rarity, death
from PENTAlore import lore, books



# Area and Zone Data

zones = {"Starting Forest": ["Zone 1: Unnamed Path", 
                             "Zone 2: Forgotten Maze", 
                             "Zone 3: Ancient World Tree", 
                             "Final Zone: Forest Harbor"],
         
         "The Middle West": ["Zone 1: Oakmere Village", 
                             "Zone 2: Aravelle Village", 
                             "Zone 3: Fernvale Village", 
                             "Zone 4: Skyhold Village", 

                             "Zone 5: Temple Emperor", 

                             "Zone 6: The Wilderness",
                             "Zone 7: Greywatch", 

                             "Zone 8: Dungeon of the Shadow Emperor", 
                             "Zone 9: The Glory Emperor's Castle",
                             "Zone 10: The Dark Emperor's Lair",
                             "Zone 11: Keep of the Fallen Emperor",
                             "Zone 12: The Lost Fortress",
                             "Zone 13: The Eternal Citadel",
                             "Zone 14: The Tower of Eternity",

                             "Zone 15: Ancient Battlefield",
                             "Zone 16: Zone of Trials",

                             "Zone 17: Willowford Town",
                             "Zone 18: Duskwood Town",

                             "Zone 19: The Imperial Outpost",

                             "Zone 20: Ravencrest City",
                             "Zone 21: Ironcrest City",
                             "Zone 22: Virecrest City",
                             "Zone 23: Mooncrest City"
                             "Final Zone: Headmaster Alina's Mansion"],


         "Sefirot Academy": ["Zone 1: Academy Entrance",
                             "Zone 2: Auditorium",

                             "Zone 3: Class 2A - Sefirot Studies II",
                             "Zone 4: Class 2B - Sefirot Combat II",
                             "Zone 5: Class 2C - World History",

                             "Zone 6: Library",
                             "Zone 7: Academy Restaurant",
                             "Zone 8: Sparring Arena",
                             "Zone 9: Dormrooms",

                             "Zone 10: Headmaster's Office",

                             "Zone 11: School Rooftop",
                             "Zone 11: Academy Lab", 
                             "Zone 12: Music Room", 
                             "Zone 13: The Hub", 

                             "Zone 14: Academy Dungeon",

                             "Zone 15: Class 3A - Sefirot Applications",
                             "Zone 16: Class 3B - Advanced Combat",
                             "Zone 17: Class 3C - Sefirot Applications II",

                             "Zone 18: Gymnasium",

                             "Zone 19: Class 1A - Sefirot Studies I",
                             "Zone 20: Class 1B - Sefirot Combat I",
                             "Zone 21: Class 1C - Introduction to Deities",

                             "Zone 22: Festival Grounds",
                             "Zone 23: Infirmary",
                             "Zone 24: Observatory",
                             "Zone 25: Staff Room",

                             "Zone 26: Sefirot Measurement Lab",

                             "Zone 27: (Maybe Illegal) Gambling Room",
                             "Zone 28: Underground Fight Club",

                             "Zone 29: Transportation Hub",

                             "Zone 30: Training Room X",

                             "Final Zone: Sefirot Tower"],
        
         "Haven City": ["Zone 1: Home",
                        "Zone 2: The Immortal's Gamble",
                        "Zone 3: ARENA X",
                        "Zone 4: The Haven Building",
                        "Zone 5: Skybridge",
                        "Final Zone: The Core"],

         "The Empire": ["Zone 1: The Imperial Gateway",
                        "Zone 2: Imperial Palace Alpha",
                        "Zone 3: Imperial Palace Omega",
                        "Zone 4: Lake of Memories",
                        "Final Zone: The Throne Room"],

         "Mount Olympus": ["Zone 1: Unnamed Path",
                           "Zone 2: Unnamed Path",
                           "Zone 3: Unnamed Path",
                           "Zone 4: Unnamed Path",
                           "Zone 5: Unnamed Path"],
         
         "The Promised Land": ["Zone 1: Unnamed Path",
                               "Zone 2: Unnamed Path",
                               "Zone 3: Unnamed Path",
                               "Zone 4: Unnamed Path", 
                               "Zone 5: Unnamed Path"],


         "Serpent's Lair": ["Zone 1: Unnamed Path",
                            "Zone 2: Unnamed Path",
                            "Zone 3: Unnamed Path",
                            "Zone 4: Unnamed Path",
                            "Zone 5: Unnamed Path"]
         }



weapons = {# Shiny Sword varients
           "'Shiny Sword' {Rare}": {"Description": "A useless sword that offers no benefits but its aesthetic appeal.",
                                    "Craft": ["Uncraftable"]},
           "'Shiny Sword Alpha' {Epic}": {"Strength": +100, "Mana": +100, "Description": "A sword that offers more benefits than just its aesthetic appeal.",
                                    "Craft": ["Uncraftable"]},
           "'Shiny Sword Omega' {Legendary}": {"Strength": +500, "Mana": +500, "Description": "A sword that offers more benefits than just its aesthetic appeal.",
                                               "Craft": ["Uncraftable"]},
           "'Shiny Sword X' {Mythic}": {"Strength": +1000, "Mana": +1000, "Description": "A sword that offers more benefits than just its aesthetic appeal.",
                                         "Craft": ["Uncraftable"]},
           "'Shiny Sword XX' {Divine}": {"Strength": +5000, "Mana": +5000, "Description": "A sword that offers more benefits than just its aesthetic appeal.",
                                         "Craft": ["Uncraftable"]},
           "'Shiny Sword XXX' {Special}": {"Strength": +10000, "Mana": +10000, "Description": "A sword that offers more benefits than just its aesthetic appeal.",
                                             "Craft": ["Uncraftable"]},
           "'Shiny Sword EX' {Special}": {"Strength": +50000, "Mana": +50000, "Description": "A sword that offers more benefits than just its aesthetic appeal.",
                                          "Craft": ["Uncraftable"]},

            # Saber varients
           "'Saebr' {Rare}": {"Description": "One of the most popular and iconic weapon in the Realm. A sword that is said to be able to cut through anything.",
                              "Craft": ["Uncraftable"]},
           "'Seibr' {Rare}": {"Description": "One of the most popular and iconic weapon in the Realm. A sword that is said to be able to slice through anything.",
                              "Craft": ["Uncraftable"]},
           "'Saybr' {Rare}": {"Description": "One of the most popular and iconic weapon in the Realm. A sword that is said to be able to pierce through anything.",
                              "Craft": ["Uncraftable"]},

            # Stick variants            
           "'Stick' {Common}": {"Strength": +3, "Description": "A regular stick.",
                                "Craft": ["Uncraftable"]},
           "'Magic Stick' {Rare}": {"Mana": +100, "Description": "A not-so-regular stick infused with mana.",
                                    "Craft": ["Uncraftable"]},
           "'Mana Stick' {Epic}": {"Mana": +500, "Description": "A stick infused with a large amount of mana.",
                                    "Craft": ["'Magic Stick' {Rare}", "'Stick' {Common}", "'Mana Dust' {Epic}"]},
           "'Essence of Stick' {Legendary}": {"Mana": +1000, "Description": "A stick infused with an abnormal large amount of mana.",
                                               "Craft": ["'Mana Stick' {Epic}", "'Magic Stick' {Rare}", "'Stick' {Common}"]},
           "'Stick of the Gods' {Mythic}": {"Mana": +5000, "Description": "A stick infused with an amount of mana, almost as if it was used by a God...",
                                            "Craft": ["'Essence of Stick' {Legendary}", "'Mana Stick' {Epic}", "'Mana Essence' {Legendary}"]},
           "'Ultimate Stick' {Divine}": {"Mana": +10000, "Description": "A ridiculous stick with absurd mana.",
                                        "Craft": ["'Stick of the Gods' {Mythic}", "'Mana Core' {Mythic}"]},

            # Classic variants
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

            # Gun variants
           "'Gun' {Legendary}": {"Strength": +2000, "Description": "A frickin gun.",
                                 "Craft": ["Uncraftable"]},
           "'Gun (Sefirot Tuned)' {Legendary}": {"Strength": +2000, "Mana": +500, "Description": "A frickin gun... but with a bit of magic...",
                                         "Craft": ["'Gun' {Legendary}", "'Mana Dust' {Epic}"]},
           "'Gun (Malkhut Tuned)' {Legendary}": {"Strength": +2000, "Health": +500, "Description": "A frickin gun... but with a bit of health...",
                                         "Craft": ["'Gun (Sefirot Tuned)' {Legendary}"]},
           "'Gun (Yesod Tuned)' {Legendary}": {"Strength": +2000, "Mana": +500, "Health": +500, "Description": "A frickin gun... but with a bit of magic and health...",
                                         "Craft": ["'Gun (Sefirot Tuned)' {Legendary}"]},
            #ADD JEWELS QUICK

            # Scythe variants
           "'Scythe' {Rare}": {"Strength": +100, "Health": -100, "Mana": +200, "Description": "A scythe with a sickly aura around it.",
                               "Craft": ["Uncraftable"]},
           "'Drain Scythe' {Epic}": {"Strength": +350, "Health": -200, "Mana": +750, "Description": "A scythe made of a worthy adventurer's bones. Imbued with an effect that drains the user's life permanently.",
                                            "Craft": ["'Bone' {Common}", "'Bone' {Common}", "'Bone' {Common}", "'Mana Dust' {Epic}", "'Scrap' {Common}"]},
           "'Drainer Scythe' {Legendary}": {"Strength": +1000, "Health": +1000, "Mana": +1500, "Description": "A scythe made of a worthy adventurer's bones. Imbued with a lifesteal effect.",
                                            "Craft": ["'Drain Scythe' {Epic}", "'Mana Essence' {Legendary}", "'Bone' {Common}"]},
           "'Death Scythe' {Epic}": {"Strength": +500, "Health": -300, "Mana": +800, "Description": "A scythe forged from the weapons of a worthy advernturer. Imbued with an effect that drains the user's life permanently.",
                                     "Craft": ["Uncraftable"]},
           "'Deathbringer Scythe' {Legendary}": {"Strength": +500, "Health": +250, "Mana": +2300, "Description": "A scythe forged from the weapons of a worthy adventurer. Imbued with a lifesteal effect.",
                                                 "Craft": ["'Death Scythe' {Epic}", "'Mana Essence' {Legendary}"]},
                

            # Time variants
           "'Mana Clock' {Epic}": {"Mana": +1000, "Dodge": +10, "Critical": +50, "Description": "A clock that seems to be infused with mana.",
                                   "Craft": ["Uncraftable"]},
           "'Time Watch' {Legendary}": {"Strength": +1000, "Health": +1000, "Mana": +1000, "Dodge": +20, "Critical": +100, "Description": "A watch that seems to be infused with the essence of time itself.",
                                        "Craft": ["'Mana Clock' {Epic}", "'Mana Essence' {Legendary}", "'Time Essence' {Legendary}"]},
            
            # Miscellaneous variants
           "'Eel-Shark Ball' {Epic}": {"Strength": +100, "Health": +100, "Description": "A mysterious ball that seems to contain the essence of an eel and a shark.",
                                       "Craft": ["Uncraftable"]},
           "'Light Blade' {Rare}": {"Strength": +50, "Health": +50, "Description": "A blade that glows with a soft light.",
                                   "Craft": ["Uncraftable"]},
           "'Tennis Racket' {Common}": {"Strength": +10, "Health": +10, "Description": "A racket used for playing tennis.",
                                         "Craft": ["'Stick' {Common}", "'Scrap' {Common}"]}}


armor = {"'Leather Armor' {Common}": {"Defense": +10, "Health": +10, "Description": "Armor made from toughened leather.",
                                      "Craft": ["'Leather' {Common}", "'Leather' {Common}", "'Leather' {Common}"]},
         "'Moss Armor' {Common}": {"Defense": +5, "Dodge": +1, "Description": "Horrible armor made of moss.",
                                   "Craft": ["'Moss' {Common}", "'Moss' {Common}", "'Moss' {Common}"]},
         "'Scrap Armor' {Common}": {"Defense": +7, "Description": "Horrible armor made up of random metal objects.",
                                    "Craft": ["'Scrap' {Common}", "'Scrap' {Common}", "'Scrap' {Common}"]},
         "'Iron Armor' {Uncommon}": {"Defense": +40, "Health": +20, "Description": "A sturdy armor forged from iron.",
                                     "Craft": ["'Iron' {Uncommon}", "'Iron' {Uncommon}", "'Iron' {Uncommon}"]},
         "'Bronze Armor' {Uncommon}": {"Defense": +150, "Health": +77, "Description": "A sturdy armor forged from bronze.",
                                        "Craft": ["'Bronze' {Uncommon}", "'Bronze' {Uncommon}", "'Bronze' {Uncommon}"]},
         "'Crown of Kings' {Legendary}": {"Description": "A crafted crown only used by ancient royalty. It is said to grant the wearer immense power.",
                                          "Craft": ["Uncraftable"]}}


items = {"'Health Potion' {Common}": {"Heal": 100, "Description": "A potion that heals 100 health.",
                                      "Craft": ["Uncraftable"]},
         "'Mana Potion' {Common}": {"Restore": 100, "Description": "A potion that restores 100 mana.",
                                    "Craft": ["Uncraftable"]},
                                    
         "'Rejamesinator' {Rare}": {"Heal": 2500, "Description": "A bean with powerful healing powers.",
                                   "Craft": ["Uncraftable"]},
                                   
         "'Forest Key' {Epic}": {"Description": "A key that unveils the secrets of the Starting Forest.",
                                "Craft": ["'Stick' {Common}", "'Moss' {Common}",  "'Scrap' {Common}"]},
         "'Stone Key' {Epic}": {"Description": "A key that unveils the secrets of the Forgotten Maze.",
                                "Craft": ["'Stick' {Common}", "'Stone' {Common}",  "'Scrap' {Common}"]},

         "'RAM' {Legendary}": {"Description": "A stick of RAM that can be used to boost your computer's performance. Very saught after.",
                              "Craft": ["Uncraftable"]}}


crafting_items = {"'Bronze' {Uncommon}": {"Description": "A material that is a mixture of copper and tin.",
                                          "Craft": ["'Copper' {Uncommon}", "'Tin' {Uncommon}"]},
                  "'Brass' {Uncommon}": {"Description": "A material that is a mixture of copper and zinc.",
                                         "Craft": ["'Copper' {Uncommon}", "'Zinc' {Uncommon}"]},
    
                  "'Sterling Silver' {Rare}": {"Description": "A precious metal that is a mixture of silver and copper.",
                                              "Craft": ["'Silver' {Uncommon}", "'Copper' {Uncommon}"]},
                  "'White Gold' {Rare}": {"Description": "A precious metal that is a mixture of gold and zinc.",
                                          "Craft": ["'Gold' {Uncommon}", "'Zinc' {Uncommon}"]},
                  "'Electrum' {Rare}": {"Description": "A precious metal that is a mixture of gold and silver.",
                                        "Craft": ["'Gold' {Uncommon}", "'Silver' {Uncommon}"]},
                  "'Inconel' {Epic}": {"Description": "A material that is a mixture of nickel, iron, and chromium.",
                                       "Craft": ["'Nickel' {Uncommon}", "'Iron' {Uncommon}", "'Chromium' {Uncommon}"]},
                  "'Rose Gold' {Epic}": {"Description": "A precious metal that is a mixture of gold, silver, and copper.",
                                         "Craft": ["'Gold' {Uncommon}", "'Silver' {Uncommon}", "'Copper' {Uncommon}"]}}


all_items = weapons | armor | items | crafting_items


drops = {"'Stick' {Common}": {"Description": "A regular stick."},
         "'Moss' {Common}": {"Description": "A flowerless plant that can be used to craft armor."},
         "'Scrap' {Common}": {"Description": "A variety of useless metallic items formed into a ball-like shape."},
         "'Leather' {Common}": {"Description": "A somewhat durable and flexible material."},
         "'Stone' {Common}": {"Description": "A rock."},
         "'Bone' {Common}": {"Description": "A piece of bone from a deceased creature."},
         "'Zinc' {Common}": {"Description": "A material that can be used in a variety of ways."},
         "'Copper' {Common}": {"Description": "A smelted material that can be used in a variety of ways."},
         "'Nickel' {Common}": {"Description": "A smelted material that can be used in a variety of ways."},
         "'Tin' {Common}": {"Description": "A smelted material that can be used in a variety of ways."},
         "'Wood' {Common}": {"Description": "A foraged material."},
        
         "'Iron' {Uncommon}": {"Description": "A smelted material that can be used in a variety of ways."},
         "'Obsidian' {Uncommon}": {"Description": "A volcanic glass with great toughness."},
         "'Bronze' {Uncommon}": {"Description": "A material that is a mixture of copper and tin."},
         "'Brass' {Uncommon}": {"Description": "A material that is a mixture of copper and zinc."},
         "'Silver' {Uncommon}": {"Description": "A precious metal that can be used in a variety of ways."},
         "'Gold' {Uncommon}": {"Description": "A precious metal that can be used in a variety of ways."},
         "'Chromium' {Uncommon}": {"Description": "A precious metal that can be used in a variety of ways."},
        
         "'Magic Stick {Rare}": {"Description": "A not-so-regular stick infused with mana."},
         "'Sterling Silver' {Rare}": {"Description": "A precious metal that is a mixture of silver and copper."},
         "'White Gold' {Rare}": {"Description": "A precious metal that is a mixture of gold and zinc."},
         "'Electrum' {Rare}": {"Description": "A precious metal that is a mixture of gold and silver."},

         "'Mana Dust' {Epic}": {"Description": "A physical manifestation of mana in a powdery-like form."},
         "'Inconel' {Epic}": {"Description": "A material that is a mixture of nickel, iron, and chromium."},
         "'Rose Gold' {Epic}": {"Description": "A precious metal that is a mixture of gold, silver, and copper."},

         "'Mana Essence' {Legendary}": {"Description": "A physical manifestation of mana in a sphere-like form."},
         "'Flower Core' {Legendary}": {"Description": "A physical manifestation of a creature's connection to nature."},
         "'Steel Core' {Legendary}": {"Description": "A physical manifestation of a creature's connection to the underground."},
         "'Xirce Core' {Legendary}": {"Description": "A physical manifestation of a creature's connection to the divine."},
         "'Hycro Core' {Legendary}": {"Description": "A physical manifestation of a creature's connection to the divine."},
         "'Time Essence' {Legendary}": {"Description": "A physical manifestation of a creature's connection to time."},

         "'Mana Core' {Mythic}": {"Description": "A physical manifestation of a creature's connection to mana."}}



#add op stuff but super rare chance
enemy_loot_tables = {"Mossling": {"Loot": ["'Stick' {Common}", "'Moss' {Common}", "'Moss' {Common}", "'Scrap' {Common}", "'Leather' {Common}", "'Iron' {Uncommon}", "'Flower Core' {Legendary}"], 
                                  "Chance": [50, 100, 45, 25, 25, 15, 1]},
                     "Pebblekin": {"Loot": ["'Stick' {Common}", "'Stone' {Common}", "'Scrap' {Common}", "'Iron' {Uncommon}", "'Steel Core' {Legendary}"], 
                                   "Chance": [50, 50, 25, 20, 1]},
                     "Forest Wisp": {"Loot": ["'Moss' {Common}", "'Magic Stick' {Rare}", "'Mana Dust' {Epic}", "'Mana Essence' {Legendary}'", "'Mana Core' {Mythic}"], 
                                     "Chance": [75, 5, 3, 1, 0.1]},
                     "Rock Golem": {"Loot": ["'Scrap' {Common}", "'Iron' {Uncommon}", "'Iron' {Uncommon}", "'Mana Essence' {Legendary}", "'Steel Core' {Legendary}"],
                                   "Chance": [100, 75, 50, 2, 2]}
                                     
}


def get_loot(enemy):
    temp_list = []
    quick_text("╔══════════════ LOOT ══════════════╗")
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
                legendary = random.choice([f"LEGENDARY DROP! You have obtained a {enemy_loot_tables[enemy]["Loot"][loot]}.", 
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
    global weapons
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
            if crafting_circle == ["'Wood' {Common}"]:
                for _ in range(3):
                    character["Inventory"].append("'Stick' {Common}")
                rarity_of_craft = recipe.split()[-1].upper().replace("{", "").replace("}", "")
                x = random.choice([f"COMMON CRAFT! You have created 3 sticks.",
                                      f"COMMON CRAFT! You have successfully made 3 sticks.",
                                      f"COMMON CRAFT! You have made 3 sticks.",
                                      f"COMMON CRAFT! You have crafted 3 sticks.",
                                      f"COMMON CRAFT! The crafting void reveals 3 sticks.",
                                      f"COMMON CRAFT! 3 sticks floats out of the crafting void",
                                      f"COMMON CRAFT! 3 sticks has been created."])
                quick_text(x)
                input_to_clear()
                continue
                
            some_random_variable = "no"
            for recipe in all_items.keys():
                if sorted(crafting_circle) == sorted(all_items.get(recipe).get("Craft")):
                    character["Inventory"].append(recipe)
                    rarity_of_craft = recipe.split()[-1].upper().replace("{", "").replace("}", "")
                    x = random.choice([f"{rarity_of_craft} CRAFT! You have created a {recipe}.",
                                      f"{rarity_of_craft} CRAFT! You have successfully made a {recipe}.",
                                      f"{rarity_of_craft} CRAFT! You have made a {recipe}.",
                                      f"{rarity_of_craft} CRAFT! You have crafted a {recipe}.",
                                      f"{rarity_of_craft} CRAFT! The crafting void reveals a {recipe}.",
                                      f"{rarity_of_craft} CRAFT! A {recipe} floats out of the crafting void",
                                      f"{rarity_of_craft} CRAFT! A {recipe} has been created."])
                    quick_text(x)
                    input_to_clear()
                    some_random_variable = "yes"
                    break
                else:
                    pass
            
            if some_random_variable == "no":
                for item in crafting_circle:
                    character["Inventory"].append(item)
                crafting_circle = []
                x = random.choice(["The crafting circle spews back the inserted materials back at you",
                                        "Nothing was crafted.",
                                        "The crafting circle reveals no item",
                                        "Your attempt at crafting has failed",
                                        "Better luck next time. Nothing was created.",
                                        "NO CRAFT!",
                                        "Crafting attempt unsuccessful.",
                                        "Crafting was unsuccessful."])
                quick_text(x)
                input_to_clear()
                continue
            else:
                crafting_circle = []
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
        clear()
        if decision_s == "b" or decision_s == "back" or decision_s == "B" or decision_s == "Back":
            break
        try:
            decision_s = int(decision_s)
        except ValueError:
            quick_text("Invalid input.")
            input_to_continue()
            continue
        else:
            decision_s = round(decision_s, 2)
            if decision_s <= 0:
                quick_text("That is not possible.")
                input_to_continue()
                continue
            elif character["POTENTIAL"] < decision_s:
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
        clear()
        if decision_s == "b" or decision_s == "back" or decision_s == "B" or decision_s == "Back":
            break
        try:
            decision_s = int(decision_s)
        except ValueError:
            quick_text("Invalid input.")
            input_to_continue()
            continue
        else:
            decision_s = round(decision_s, 2)
            if decision_s <= 0:
                quick_text("That is not possible.")
                input_to_continue()
                continue
            elif character[attribute] < decision_s:
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
            type_text(f"Zone Name: {zones[character['Location'].split('Zone')[0].strip()][0]}")
            type_text(f"Current Coordinate: {character['Coordinates']}")
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


    
def inventory():
    global character, weapons, armor, items, all_items, drops, books
    craft_description_list = ["Craft", "Description"]
    while True:
        character["Inventory"] = rarity_sort(character["Inventory"])
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
                    input_to_clear()
                    if character["Health"] <= 0:
                        type_text(f"You have died from equipping the {list_of_items[x]} due to its negative effects.")
                        input_to_clear()
                        death()
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
                    input_to_clear()
                    if character["Health"] <= 0:
                        type_text(f"You have died from equipping the {list_of_items[x]} due to its negative effects.")
                        input_to_clear()
                        death()
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
    


def loot_sort(lootpool, storage):
    global character
    type_of_storage = storage.split("_")[0]
    for loot in lootpool:
        chance = lootpool[loot] / (100 - character["Luck"] * 0.5)
        roll = random.random()
        if roll <= chance:
            character["Inventory"].append(loot)
            rarity(loot)
    character["Inventory"] = rarity_sort(character["Inventory"])
    character[type_of_storage][storage] = True
    input_to_clear()
    

def loot_drops(storage):
    global character
    type_of_storage = storage.split("_")[0]
    clear()
    if type_of_storage == "Chest":
        if storage == "Chest_1":
            quick_text("╔══════════════ CHEST ══════════════╗")
            chest_loot = {"'Leather' {Common}": 100, "'Stick' {Common}": 100, "'Wood' {Common}": 100,
                          "'Leather Armor' {Common}": 20, "'Scrap Armor' {Common}": 20, 
                          "'Stone Hammer' {Common}": 20, "'Stone Sword' {Common}": 20, "'Stone Shield' {Common}": 20,
                          "'Iron' {Uncommon}": 50, "'Iron Dagger' {Uncommon}": 5, "'Forest Key' {Epic}": 5,
                          "'Mana Dust' {Epic}": 3, "'Mana Essence' {Legendary}": 1} 
            loot_sort(chest_loot, storage)
        
        elif storage == "Chest_2":
            quick_text("╔══════════════ CHEST ══════════════╗")
            chest_loot = {"'Scrap Armor' {Common}": 20, 
                          "'Stone Spear' {Common}": 50, "'Stone Sword' {Common}": 50, "'Stone Dagger' {Common}": 50,
                          "'Nickel' {Common}": 50, "'Zinc' {Common}": 50, "'Tin' {Common}": 50,
                          "'Iron' {Uncommon}": 50, "'Iron Dagger' {Uncommon}": 50, "'Stone Key' {Epic}": 50,
                          "'Mana Dust' {Epic}": 3, "'Steel Core' {Legendary}": 2, "'Mana Essence' {Legendary}": 1}
            loot_sort(chest_loot, storage)

        elif storage == "Chest_3":
            quick_text("╔══════════════ CHEST ══════════════╗")
            chest_loot = {"'Drain Scythe' {Epic}": 100, "'Stone Key' {Epic}": 50}
            loot_sort(chest_loot, storage)

        elif storage == "Chest_4":
            quick_text("╔══════════════ CHEST ══════════════╗")
            chest_loot = {"'Copper' {Common}": 100, "'Moss' {Common}": 100, "'Bone' {Common}": 98, "'Scrap' {Common}": 97, "'Leather' {Common}": 96,
                          "'Iron' {Uncommon}": 95, "'Silver' {Uncommon}": 94, "'Sterling Silver' {Rare}": 55, "'Mana Dust' {Epic}": 30, "'Xirce Core' {Legendary}": 1}
            loot_sort(chest_loot, storage)
        
        elif storage == "Chest_5":
            quick_text("╔══════════════ CHEST ══════════════╗")
            chest_loot = {"'Leather' {Common}": 100, "'Stick' {Common}": 100, "'Wood' {Common}": 100, "'Scrap' {Common}": 20, 
                          "'Iron Hammer' {Uncommon}": 20, "'Iron Sword' {Uncommon}": 20, "'Iron Shield' {Uncommon}": 20,
                          "'Iron' {Uncommon}": 50, "'Iron Dagger' {Uncommon}": 5, "'Stone Key' {Epic}": 10,
                          "'Mana Dust' {Epic}": 4.5, "'Mana Essence' {Legendary}": 2.2} 
            loot_sort(chest_loot, storage)
        
        elif storage == "Chest_6":
            quick_text("╔══════════════ CHEST ══════════════╗")
            chest_loot = {"'Tin' {Common}": 100, "'Nickel' {Common}": 100, "'Iron' {Uncommon}": 90,
                          "'Iron' {Uncommon}": 20, "'Iron Armor {Uncommon}": 50, "'Bronze' {Uncommon}": 50,
                          "'Stone Key' {Epic}": 10, "'Mana Dust' {Epic}": 4.5, "'Mana Essence' {Legendary}": 2.2} 
            loot_sort(chest_loot, storage)
        
        elif storage == "Chest_7":
            ...


    elif type_of_storage == "Barrel":
        if storage == "Barrel_1":
            quick_text("╔══════════════ BARREL ══════════════╗")
            barrel_loot = {"'Stone' {Common}": 100, "'Stick' {Common}": 100, "'Wood' {Common}": 100, "'Stone Dagger' {Common}": 50,
                           "'Stone Spear' {Common}": 30, "'Stone Shield' {Common}": 50,
                           "'Iron' {Uncommon}": 50, "'Mana Essence' {Legendary}": 3,
                           "'Steel Core' {Legendary}": 3}
            loot_sort(barrel_loot, storage)
        
        elif storage == "Barrel_2":
            quick_text("╔══════════════ BARREL ══════════════╗")
            barrel_loot = {"'Stone' {Common}": 100, "'Stone' {Common}": 95, "'Wood' {Common}": 100,
                           "'Bone' {Common}": 75, "'Zinc' {Common}": 75, "'Copper' {Common}": 75,
                           "'Magic Stick {Rare}": 5, "'Mana Dust' {Epic}": 1}
            loot_sort(barrel_loot, storage)
        
        elif storage == "Barrel_3":
            quick_text("╔══════════════ BARREL ══════════════╗")
            barrel_loot = {"'Stone' {Common}": 100, "'Stone' {Common}": 95, "'Wood' {Common}": 100,
                           "'Mana Dust' {Epic}": 5, "'Mana Essence' {Legendary}": 1, "'Steel Core' {Legendary}": 1}
            loot_sort(barrel_loot, storage)
        
        elif storage == "Barrel_4":
            quick_text("╔══════════════ BARREL ══════════════╗")
            barrel_loot = {"'Stone' {Common}": 100, "'Wood' {Common}": 100,
                           "'Nickel' {Common}": 100, "'Nickel' {Common}": 20, "'Copper' {Common}": 50, "'Copper' {Common}": 50, "'Tin' {Common}": 50,
                           "'Mana Dust' {Epic}": 20, "'Mana Essence' {Legendary}": 5, "'Steel Core' {Legendary}": 5}
            loot_sort(barrel_loot, storage)
        
        elif storage == "Barrel_5":
            quick_text("╔══════════════ BARREL ══════════════╗")
            barrel_loot = {"'Stone' {Common}": 100, "'Stick' {Common}": 100, "'Wood' {Common}": 100, "'Iron Dagger' {Uncommon}": 50,
                           "'Iron Spear' {Uncommon}": 30, "'Iron Shield' {Uncommon}": 50, "'Iron' {Uncommon}": 50,
                           "'Mana Dust' {Epic}": 70, "'Mana Dust' {Epic}": 35, "'Mana Dust' {Epic}": 10, 
                           "'Mana Essence' {Legendary}": 3, "'Steel Core' {Legendary}": 3}
            loot_sort(barrel_loot, storage)

        elif storage == "Barrel_6":
            ...


    elif type_of_storage == "Corpse":
        if storage == "Corpse_1":
            quick_text("╔══════════════ CORPSE ══════════════╗")
            corpse_loot = {"'Scrap Armor' {Common}": 100, "'Stick' {Common}": 100, "'Stick' {Common}": 50, "'Zinc' {Common}": 50,
                           "'Forest Key' {Epic}": 100, "'Forest Key' {Epic}": 50}
            loot_sort(corpse_loot, storage)
        
        elif storage == "Corpse_2":
            quick_text("╔══════════════ CORPSE ══════════════╗")
            corpse_loot = {"'Iron Hammer' {Uncommon}": 100}
            loot_sort(corpse_loot, storage)
        
        elif storage == "Corpse_3":
            quick_text("╔══════════════ CORPSE ══════════════╗")
            corpse_loot = {"'Stone Key' {Uncommon}": 100,"'Mana Dust' {Epic}": 100, "'Mana Essence' {Legendary}": 5}
            loot_sort(corpse_loot, storage)

        elif storage == "Corpse_4":
            quick_text("╔══════════════ CORPSE ══════════════╗")
            corpse_loot = {"'Stone Key' {Uncommon}": 100, "'Gold' {Uncommon}": 100, "'White Gold' {Rare}": 50, "'Time Essence' {Legendary}": 5}
            loot_sort(corpse_loot, storage)

        elif storage == "Corpse_5":
            quick_text("╔══════════════ CORPSE ══════════════╗")
            corpse_loot = {"'Stone Key' {Uncommon}": 50, "'Gold' {Uncommon}": 50, "'Hycro Core' {Legendary}": 100}
            loot_sort(corpse_loot, storage)
        
        elif storage == "Corpse_6":
            quick_text("╔══════════════ CORPSE ══════════════╗")
            corpse_loot = {"'Stone Key' {Uncommon}": 50, "'Silver' {Uncommon}": 50, "'Xirce Core' {Legendary}": 100}
            loot_sort(corpse_loot, storage)

        elif storage == "Corpse_7":
            quick_text("╔══════════════ CORPSE ══════════════╗")
            corpse_loot = {"'Magic Stick' {Rare}": 100}
            loot_sort(corpse_loot, storage)
        
        elif storage == "Corpse_8":
            quick_text("╔══════════════ CORPSE ══════════════╗")
            corpse_loot = {"'Scythe' {Rare}": 100}
            loot_sort(corpse_loot, storage)


    elif type_of_storage == "Cache":
        if storage == "Cache_1":
            quick_text("╔══════════════ CACHE ══════════════╗")
            cache_loot = {"'Stone' {Common}": 100, "'Stone' {Common}": 90, "'Stone' {Common}": 50,
                          "'Stick' {Common}": 100, "'Stick' {Common}": 50, "'Stick' {Common}": 25,
                           "'Iron' {Uncommon}": 100, "'Iron' {Uncommon}": 90, "'Iron' {Uncommon}": 50,
                           "'Stone Key' {Uncommon}": 75,
                           "'Iron Armor' {Uncommon}": 30,
                           "'Mana Essence' {Legendary}": 10,
                           "'Steel Core' {Legendary}": 10}
            loot_sort(cache_loot, storage)
        
        elif storage == "Cache_2":
            quick_text("╔══════════════ CACHE ══════════════╗")
            cache_loot = {"'Stone' {Common}": 100, "'Wood' {Common}": 100,
                          "'Bone' {Common}": 75, "'Zinc' {Common}": 75, "'Copper' {Common}": 75, "'Nickel' {Common}": 75, "'Tin' {Common}": 75,
                          "'Iron' {Uncommon}": 100, "'Iron' {Uncommon}": 50, "'Obsidian' {Uncommon}": 50, "'Bronze' {Uncommon}": 50,
                          "'Silver {Uncommon}": 50, "'Gold' {Uncommon}": 50, "'Chromium' {Uncommon}": 50,
                          "'Stone Key' {Uncommon}": 75, "'Iron Armor' {Uncommon}": 20, "'Iron Shield' {Uncommon}": 20, "'Iron Hammer' {Uncommon}": 20, "'Iron Spear' {Uncommon}": 20,
                          "'Mana Dust' {Epic}": 10, "'Inconel' {Epic}": 10, "'Steel Core' {Legendary}": 5}
            loot_sort(cache_loot, storage)
        
        elif storage == "Cache_3":
            quick_text("╔══════════════ CACHE ══════════════╗")
            cache_loot = {"'Iron' {Uncommon}": 100, "'Iron' {Uncommon}": 50, "'Iron' {Uncommon}": 25, "'Obsidian' {Uncommon}": 100, "'Obsidian' {Uncommon}": 33,
                          "'Bronze' {Uncommon}": 50, "'Bronze' {Uncommon}": 50, "'Silver {Uncommon}": 71, "'Gold' {Uncommon}": 29, "'Chromium' {Uncommon}": 10}
            loot_sort(cache_loot, storage)

        elif storage == "Cache_4":
            quick_text("╔══════════════ CACHE ══════════════╗")
            cache_loot = {"'Scrap' {Common}": 100, "'Leather' {Common}": 100, "'Bone' {Common}": 90, "'Copper' {Common}": 100, "'Nickel' {Common}": 95, "'Tin' {Common}": 100,
                          "'Iron' {Uncommon}": 100, "'Iron' {Uncommon}": 90, "'Bronze' {Uncommon}": 85, "'Silver' {Uncommon}": 75, "'Gold' {Uncommon}": 75,
                          "'Magic Stick' {Rare}": 100, "'Magic Stick' {Rare}": 35, "'Sterling Silver' {Rare}": 50, "'White Gold' {Rare}": 50, "'Electrum' {Rare}": 30,
                          "'Mana Dust' {Epic}": 100, "'Mana Dust' {Epic}": 35, "'Mana Dust' {Epic}": 5, "'Mana Essence' {Legendary}": 3, "'Time Essence' {Legendary}": 3, "'Mana Core' {Mythic}": 2}
            loot_sort(cache_loot, storage)

        elif storage == "Cache_5":
            quick_text("╔══════════════ CACHE ══════════════╗")
            cache_loot = {"'Bone' {Common}": 100, "'Copper' {Common}": 100, "'Iron' {Uncommon}": 90, "'Brass' {Uncommon}": 90, "'Silver' {Uncommon}": 90, "'Chromium' {Uncommon}": 80,
                          "'Sterling Silver' {Rare}": 75, "'Electrum' {Rare}": 75, "'Magic Stick' {Rare}": 65,
                          "'Mana Dust' {Epic}": 50, "'Rose Gold' {Epic}": 20, "'Flower Core' {Legendary}": 10, "'Hycro Core' {Legendary}": 5.5}
            loot_sort(cache_loot, storage)
        
        elif storage == "Cache_6":
            ...





def lore_drops(lore_number):
    global character
    clear()
    if lore_number == "Lore_1":
        text = ["You find yourself in a slightly more swampy area of the forest.",
                            "In the corner of your eye, you see something."]
        monologue(text)
        while True:
            text = ["You discover a dusty book with a leather cover.",
                    "The pages seem slightly moldy and weathered.",
                    "What do you do?"]
            monologue(text)
            x = question_input("Pick up the book (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the book and put it in your inventory.")
                type_text("The title of the book reads 'Houlester's Guide to the 10 Sefirots'.")
                character["Inventory"].append("'Houlester's Guide to the 10 Sefirots' {DAMAGED}")
                character["Lore"]["Lore_1"] = True
                character["Inventory"] = rarity_sort(character["Inventory"])
                input_to_clear()
                break
            elif x == "m" or x == "menu":
                menu()
                continue
            else:
                clear()
                type_text("You have decided to ignore the book.")
                input_to_clear()
                break

    elif lore_number == "Lore_2":
        text = ["You walk inside the wrecked wooden house.",
                "Stumbling over its remains, you find a dusty journal on the ground.",
                "It seems heavily weathered by the elements.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the journal (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the journal and put it in your inventory.")
                character["Inventory"].append("'Jess' Journal' {DAMAGED}")
                character["Inventory"] = rarity_sort(character["Inventory"])
                character["Lore"]["Lore_2"] = True
                input_to_clear()
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You find a dusty journal on the ground.")
                type_text("It seems heavily weathered by the elements.")
                type_text("What do you do?")
                continue
            else:
                type_text("You decide to ignore the journal")
                type_text("You walk back outside.")
                input_to_clear()
                break

    elif lore_number == "Lore_3":
        text = ["You find yourself in the same old stony environment.",
                "In the corner of your eye, you spot a dusty and damaged book.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the book (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the book and put it in your inventory.")
                type_text("The title of the book reads 'The Mechanics of Buffs'.")
                character["Inventory"].append("'The Mechanics of Buffs' {DAMAGED}")
                character["Lore"]["Lore_3"] = True
                character["Inventory"] = rarity_sort(character["Inventory"])
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You spot a dusty and damaged book.")
                type_text("What do you do?")
                continue
            else:
                clear()
                type_text("You have decided to ignore the book.")
                input_to_continue()
                break
    
    elif lore_number == "Lore_4":
        text = ["You find yourself in the same old stony environment.",
                "In the corner of your eye, you spot a dusty and damaged book.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the book (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the book and put it in your inventory.")
                type_text("The title of the book reads 'The Numbered Emperors'.")
                character["Inventory"].append("'The Numbered Emperors' {DAMAGED}")
                character["Lore"]["Lore_4"] = True
                character["Inventory"] = rarity_sort(character["Inventory"])
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You spot a dusty and damaged book.")
                type_text("What do you do?")
                continue
            else:
                clear()
                type_text("You have decided to ignore the book.")
                input_to_continue()
                break

    elif lore_number == "Lore_5":
        text = ["You find yourself on a bunch of stony rubble."
                "Stumbling over the remains, you find a dusty journal on the ground.",
                "It seems heavily weathered by the elements.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the journal (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the journal and put it in your inventory.")
                character["Inventory"].append("'Dr. Victor's Journal' {DAMAGED}")
                character["Inventory"] = rarity_sort(character["Inventory"])
                character["Lore"]["Lore_5"] = True
                input_to_clear()
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You find a dusty journal on the ground.")
                type_text("It seems heavily weathered by the elements.")
                type_text("What do you do?")
                continue
            else:
                type_text("You decide to ignore the journal")
                input_to_clear()
                break

    elif lore_number == "Lore_6":
        text = ["You find youself in an area made of mostly dirt and stone.",
                "Around you are hollowed out crevaces in the walls.",
                "They seemed to be abandoned.",
                "Inside one of these crevaces is a journal with a rusty copper frame.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the journal (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the journal and put it in your inventory.")
                character["Inventory"].append("'Dr. Lucien's Journal' {DAMAGED}")
                character["Inventory"] = rarity_sort(character["Inventory"])
                character["Lore"]["Lore_6"] = True
                input_to_clear()
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You find a journal with a rusty copper frame inside a crevace.")
                type_text("It seems heavily weathered.")
                type_text("What do you do?")
                continue
            else:
                type_text("You decide to ignore the journal")
                input_to_clear()
                break

    elif lore_number == "Lore_7":
        text = ["You find yourself in a stony clearing, cleaned free from monsters.",
                "You look around and find a pedastal, where a book, perfectly intact, lies.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the book (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the book and put it in your inventory.")
                type_text("The title of the book reads 'Mechanisms of the Keys'.")
                character["Inventory"].append("'Mechanisms of the Keys' {COMPLETE}")
                character["Lore"]["Lore_7"] = True
                character["Inventory"] = rarity_sort(character["Inventory"])
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You find a pedatal, where a book, perfectly intact, lies.")
                type_text("What do you do?")
                continue
            else:
                clear()
                type_text("You have decided to ignore the pedastal.")
                input_to_continue()
                break

    elif lore_number == "Lore_8":
        text = ["You find yourself in a clearing, cleaned free from monsters.",
                "You spot a dirt-stone wall and a mossy wall in the west and east directions respectively.",
                "You look around and find a pedastal, where a book, perfectly intact, lies.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the book (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the book and put it in your inventory.")
                type_text("The title of the book reads 'Anatomy of the Hycro'.")
                character["Inventory"].append("'Anatomy of the Hycro' {COMPLETE}")
                character["Lore"]["Lore_8"] = True
                character["Inventory"] = rarity_sort(character["Inventory"])
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You find a pedatal, where a book, perfectly intact, lies.")
                type_text("What do you do?")
                continue
            else:
                clear()
                type_text("You have decided to ignore the pedastal.")
                input_to_continue()
                break

    elif lore_number == "Lore_9":
        text = ["You find yourself in a mossy-stony environment.",
                "In the corner of your eye, you spot a dusty and damaged book in the corner of two walls.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the book (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You picked up the book and put it in your inventory.")
                type_text("The title of the book reads 'The Most Iconic Weapons of The Realm'.")
                character["Inventory"].append("'The Most Iconic Weapons of The Realm' {DAMAGED}")
                character["Lore"]["Lore_9"] = True
                character["Inventory"] = rarity_sort(character["Inventory"])
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You spot a dusty and damaged book.")
                type_text("What do you do?")
                continue
            else:
                clear()
                type_text("You have decided to ignore the book.")
                input_to_continue()
                break

    elif lore_number == "Lore_10":
        text = ["You enter the makeshift house.",
                "In there, you find a few stone furniture.",
                "On a stone bookshelf, you find a single journal."]
        monologue(text)
        while True:
            x = question_input("Take the journal (a), Ignore it (anything else): ").strip().lower()
            if x == "a":
                clear()
                type_text("You take the journal and put it in your inventory.")
                character["Inventory"].append("'Tobias' Journal' {DAMAGED}")
                character["Lore"]["Lore_10"] = True
                character["Inventory"] = rarity_sort(character["Inventory"])
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You spot a dusty and damaged journal on a stone bookshelf.")
                type_text("What do you do?")
                continue
            else:
                clear()
                type_text("You have decided to ignore the journal.")
                input_to_continue()
                break

    elif lore_number == "Lore_11":
        text = ["You find yourself in the same old stony environment.",
                "In the corner of your eye, you spot a book with gold trims.",
                "What do you do?"]
        monologue(text)
        while True:
            x = question_input("Pick up the book (a), Ignore it (anything else): ").strip().lower()
            clear()
            if x == "a":
                type_text("You picked up the book and put it in your inventory.")
                type_text("The title of the book reads 'Terms & Conditions of the Duel'.")
                character["Inventory"].append("'Terms & Conditions of the Duel' {DAMAGED}")
                character["Lore"]["Lore_11"] = True
                character["Inventory"] = rarity_sort(character["Inventory"])
                break
            elif x == "m" or x == "menu":
                menu()
                type_text("You spot a gold-trimmed book.")
                type_text("What do you do?")
                continue
            else:
                type_text("You have decided to ignore the book.")
                input_to_clear()
                break

    