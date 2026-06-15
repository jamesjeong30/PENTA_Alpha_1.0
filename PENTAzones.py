import random, time
from PENTAutilities import question_input, type_text, input_to_continue, clear, monologue, quick_text, rarity_sort
from PENTAutilities import character
from PENTAitems import menu

# Starting Forest Zone/Tile

sfz1_coords = [[-967, 10], [-967, 11], [-967, 12], [-966, 12], [-966, 11], [-966, 10], [-965, 10], [-965, 11], [-965, 12]]


sfz2_coords = [[-971, 99], [-970, 99], [-969, 99], [-968, 99], [-967, 99], [-966, 99], [-965, 99], [-964, 99], [-963, 99], [-962, 99], [-961, 99], [-960, 99], [-959, 99],
               [-971, 100], [-968, 100], [-966, 100], [-965, 100], [-964, 100],
               [-971, 101], [-968, 101], [-966, 101], [-964, 101], [-962, 101], [-961, 101], [-960, 101], [-959, 101],
               [-971, 102], [-968, 102], [-966, 102], [-964, 102], [-963, 102], [-962, 102], [-960, 102], [-959, 102],
               [-971, 103], [-969, 103], [-968, 103], [-964, 103], [-959, 103],
               [-971, 104], [-970, 104], [-969, 104], [-968, 104], [-965, 104], [-963, 104], [-962, 104], [-959, 104],
               [-971, 105], [-968, 105], [-965, 105], [-963, 105], [-962, 105], [-961, 105], [-959, 105],
               [-971, 106], [-969, 106], [-968, 106], [-965, 106], [-961, 106], [-959, 106],
               [-971, 107], [-969, 107], [-968, 107], [-967, 107], [-966, 107], [-965, 107], [-964, 107], [-963, 107], [-961, 107], [-959, 107],
               [-971, 108], [-970, 108], [-967, 108], [-963, 108], [-962, 108], [-961, 108], [-960, 108], [-959, 108],
               [-971, 109], [-967, 109], [-965, 109], [-964, 109], [-963, 109], [-962, 109], [-961, 109], [-959, 109],
               [-971, 110], [-969, 110], [-965, 110], [-964, 110], [-959, 100],
               [-971, 111], [-970, 111], [-969, 111], [-968, 111], [-967, 111], [-966, 111], [-965, 111], [-964, 111], [-963, 111], [-962, 111], [-961, 111], [-960, 111], [-959, 111]]


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



def sfz2_tile():
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
            if [character["Coordinates"][0], character["Coordinates"][1] + 1] in sfz2_coords:
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
            if [character["Coordinates"][0], character["Coordinates"][1] - 1] in sfz2_coords:
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
            if [character["Coordinates"][0] + 1, character["Coordinates"][1]] in sfz2_coords:
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
            if [character["Coordinates"][0], character["Coordinates"][1] - 1] in sfz2_coords:
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



