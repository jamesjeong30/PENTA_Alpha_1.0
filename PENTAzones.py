import random, time
from PENTAutilities import question_input, type_text, input_to_continue, clear, monologue, quick_text, rarity_sort
from PENTAutilities import character
from PENTAitems import menu


# Location and Zone Data
zones = {"Starting Forest": ["Zone 1: Unnamed Path", 
                             
                             "Zone 2: May's Maze", 
                             "Zone 3: Ancient World Tree", 
                             "Final Zone: Forest Harbor"],
         
         "The Middle West": ["Zone 1: Oakmere Village", 
                             "Zone 2: The LA County", 
                             "Zone 3: Fernvale Village", 
                             "Zone 4: Crystal Peak", 

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

                             "Zone 17: Willowford",
                             "Zone 18: Duskwood Town",

                             "Zone 19: The Imperial Outpost",

                             "Zone 20: Ravencrest",
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
        
         "Haven City": ["Zone 1: Home", "Zone 2: The Immortal's Gamble", "Zone 3: ARENA X", "Zone 4: The Haven Building", "Zone 5: Skybridge", "Final Zone: The Core"],


         "The Empire": ["Zone 1: The Imperial Gateway", "Zone 2: Imperial Palace Alpha", "Zone 3: Imperial Palace Omega", "Zone 4: Lake of Memories", "Final Zone: The Throne Room"],

         "Mount Olympus": ["Zone 1: Unnamed Path", "Zone 2: Unnamed Path", "Zone 3: Unnamed Path", "Zone 4: Unnamed Path", "Zone 5: Unnamed Path"],
         
         "The Promised Land": ["Zone 1: Unnamed Path", "Zone 2: Unnamed Path", "Zone 3: Unnamed Path", "Zone 4: Unnamed Path", "Zone 5: Unnamed Path"],


         "Serpent's Lair": ["Zone 1: Unnamed Path", "Zone 2: Unnamed Path", "Zone 3: Unnamed Path", "Zone 4: Unnamed Path", "Zone 5: Unnamed Path"]
         }





sfz1_coords = [[-967, 10], [-967, 11], [-967, 12], [-966, 12], [-966, 11], [-966, 10], [-965, 10], [-965, 11], [-965, 12]]

sfz2_coords = []

sfz3_coords = []


def sfz1_tile():
    global character
    while True:
        clear()
        quick_text(f"╔═════════ Coordinates {character['Coordinates']} ═════════╗")
        decision = question_input("Move North (n), South (s), East (e), West (w), Use an Item (u), Stay (stay): ").strip().lower()
        clear()
        if decision == "stay":
            chance = random.random()
            if chance >= 0.999:
                character["Strength"] = 5555555555
                character["Mana"] = 5555555555
                character["Health"] = 5555555555
                character["Defense"] = 5555555555
                character["Mana Regen"] = 5555555555
                character["Luck"] = 5555555555
                character["Stat Inheritance"] = 5555555555
                character["Wisdom"] = 5555555555
                x = ["James: Alright...",
                     "James: You win.",
                     "James: How long did that really take.",
                     "James: You know what, that doesn't matter anymore.",
                     "James: You have proved yourself.",
                     "James: Through sheer perseverence and/or luck,",
                     "James: For the ultimate power.",
                     "You feel divine energy flowing through your body.",
                     "All of your stats has been massively increased!",
                     "James: Give one nothing and they will create a world."
                     "James: Give them the world... and they will destory it.",
                     "James: Have fun."]
                monologue(x)
                input_to_continue()
                continue
            else:
                return character["Coordinates"], None
            
        elif decision == "m" or decision == "menu":
            menu()
            continue
        elif decision == "n":
            if [character["Coordinates"][0], character["Coordinates"][1] + 1] in sfz1_coords:
                character["Coordinates"] = [character["Coordinates"][0], character["Coordinates"][1] + 1]
                return character["Coordinates"], None
            else:
                    x = random.choice(["The bushes are too thick to pass.",
                                      "The thick trees of the Starting Forest blocks your path.",
                                      "You cannot proceed in that direction.",
                                      "You face a wall of thick greenery.",
                                      "A wall of greenery blocks the direction."])
                    type_text(x)
                    input_to_continue()
                    continue
        elif decision == "s":
            if [character["Coordinates"][0], character["Coordinates"][1] - 1] in sfz1_coords:
                character["Coordinates"] = [character["Coordinates"][0], character["Coordinates"][1] - 1]
                return character["Coordinates"], None
            else:
                    x = random.choice(["The bushes are too thick to pass.",
                                      "The thick trees of the Starting Forest blocks your path.",
                                      "You cannot proceed in that direction.",
                                      "You face a wall of thick greenery.",
                                      "A wall of greenery blocks the direction."])
                    type_text(x)
                    input_to_continue()
                    continue
        elif decision == "e":
            if [character["Coordinates"][0] + 1, character["Coordinates"][1]] in sfz1_coords:
                character["Coordinates"] = [character["Coordinates"][0] + 1, character["Coordinates"][1]]
                return character["Coordinates"], None
            else:
                    x = random.choice(["The bushes are too thick to pass.",
                                      "The thick trees of the Starting Forest blocks your path.",
                                      "You cannot proceed in that direction.",
                                      "You face a wall of thick greenery.",
                                      "A wall of greenery blocks the direction."])
                    type_text(x)
                    input_to_continue()
                    continue
        elif decision == "w":
            if [character["Coordinates"][0], character["Coordinates"][1] - 1] in sfz1_coords:
                character["Coordinates"] = [character["Coordinates"][0], character["Coordinates"][1] - 1]
                return character["Coordinates"], None
            else:
                    x = random.choice(["The bushes are too thick to pass.",
                                      "The thick trees of the Starting Forest blocks your path.",
                                      "You cannot proceed in that direction.",
                                      "You face a wall of thick greenery.",
                                      "A wall of greenery blocks the direction."])
                    type_text(x)
                    input_to_continue()
                    continue
        elif decision == "u":
            clear()
            quick_text("╔═════════ PLAYER INVENTORY ═════════╗")
            character["Inventory"] = rarity_sort(character["Inventory"])
            for i, item_in_inventory in enumerate(character["Inventory"]):
                quick_text(f"{i + 1}. {item_in_inventory}")
            
            selected_item = question_input("Use item (#), Back (b): ").lower().strip()
            if selected_item == "b" or selected_item == "back":
                 continue
            try:
                selected_item = int(selected_item)
            except ValueError:
                 quick_text("Invalid Input.")
                 input_to_continue()
                 continue
            else:
                 if selected_item > len(character["Inventory"]) or selected_item <= 0:
                      quick_text("Invalid Input.")
                      input_to_continue()
                      continue
                 
                 return character["Coordinates"], character["Inventory"][selected_item - 1]
        


        else:
            type_text("Invalid input.")
            input_to_continue()
            continue



    