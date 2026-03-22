from PENTAutilities import b_character_create, input_to_continue, gibtext, clear_last_line, dot_effect, quick_monologue, rarity, type_text, quick_text, question_input, loading, monologue, clear, encounter_text, encounter, three_choices, rarity_sort, custom_text
from PENTAutilities import character, enemies, bosses
from PENTAutilities import enemy_moves, malkhut_moves
from PENTAitems import weapons, armor, items, books, menu
from PENTAbattle import astral_convergence, battle, battle_stat_analyze
from PENTAmusic import AudioManager
from PENTAitems import weapons, armor, items, books, chest_count, book_count
from PENTAitems import save_game, load_game, delete_save
import time
import random
from PENTAzones import sfz1_coords, sfz2_coords, zones
from PENTAzones import sfz1_tile


# the game storyline
def main():
    load_game()
    while True:
        # DO THIS FOR EVERY ZONE IN THE GAME
        if character["Location"] == "Starting Forest Zone 1":
            if character["Coordinates"] in sfz1_coords:
                sfz1()
            else:
                starting_forest_zone_1()
        elif character["Location"] == "Starting Forest Zone 2":
            if character["Coordinates"] in sfz2_coords:
                sfz2()
            else:
                starting_forest_zone_2()

        else:
            intro()



# the intro of the game
def intro():
    global character
    player_name = question_input("Enter your name: ")
    character["Name"] = player_name.strip().title()
    clear()
    type_text("Note: This is a text-based RPG and is heavily story carried.")
    type_text("Do not expect peak gameplay, but rather decent storytelling/immersion.")
    type_text("Your character also dies permanently if you die even once.")
    type_text("So don't skill issue I guess.")
    type_text("Thanks for taking interest in this demo.")
    type_text("The game and story will start right after this note.")
    input_to_continue()
    clear()
    type_text("You have only '1' life remaining...")
    dot_effect("Disabling respawn feature")
    input_to_continue()
    clear()
    text = [f"{character["Name"]}.",
            "The Realm is one of the many dimensions that exist within the multiverse.",
            "But one thing about The Realm makes it stand out from the rest...",
            "Gods.",
            "In The Realm, gods walk among mortals, influencing their lives and shaping their destinies.",
            "The Gods are far more powerful than any mortal being.",
            "That is because they are the very servants of the Sefirots", 
            "The ten divine attributes that govern all aspects of existence.",
            "Thus, the Gods can grant blessings, bestow curses, and even alter the very fabric of reality.",
            "In the history of the Realm, there is only one race that has ever been able to challenge the Gods...",
            "The Humans.",
            "Or more specifically, a select few Humans known as the Emperors.",
            "While the Gods do serve the Sefirots and were granted immense power from them,",
            "The Emperors have been able to tap into the power of the Sefirots themselves using a power called Mana.",
            "Through their connection to the Sefirots, The Emperors have been able to rival the Gods in power.",
            "In other words, the Emperors have studied and mastered the divine powers rather than being granted them.",
            "This has allowed them to challenge the Gods and even overthrow them on occasion.",
            "But the Emperors are few and far between.",
            "The Promised War, a great conflict between the Gods and the Emperors,",
            "ended with the defeat and the near-extinction of the Emperors,",
            "leaving spaces for humans to rise up and claim the title of Emperor for themselves.",
            "But The Promised Land stayed under the ownership of the Gods.",
            "Since then, the Gods have ruled over The Realm unchallenged.",
            "In The Realm, you are able to do whatever you want.", 
            "You can explore, fight monsters, live peacefully, or even meet powerful deities.",
            "Good luck, and..."]
    monologue(text)
    gibtext("'May the Blessing of the Gods be with you.'")
    time.sleep(0.5)
    input_to_continue()
    character["Location"] = "Starting Forest Zone 1"
    loading()


# intro to the starting forest area
def starting_forest_zone_1():
    global character
    global sfz1_coords
    text = ["You open your eyes to a bright light...",
            "As your vision clears, you find yourself in a lush forest.", 
            "The sound of birds chirping fills the air, and a gentle breeze rustles the leaves.",
            "You stand up, dust yourself off, and look around to get your bearings.", 
            "Welcome... to the Starting Forest."]
    monologue(text)
    input_to_continue()
    loading()

    text = ["You are in the Starting Forest.",
            "There is a small clearing ahead.",
            "Do you want to walk into the clearing?"]
    monologue(text)
    decision = question_input("Walk into clearing? Yes (y), No (n): ").strip().lower()
    clear()
    if decision == 'yes' or decision == 'y':
        text = ["You walk into the clearing and find a shiny sword on the ground.",
                "You pick up the sword, only for it to vanish in your hands."]
        monologue(text) 
        print("")
        quick_text("RARE FIND! 'Shiny Sword' {Rare}")
        character["Inventory"].append("'Shiny Sword' {Rare}")
        print("")
        text =  ["You hear a faint sound..."
                "You look around, searching for the source of the voice.",
                "Suddenly, someone fades into vision before you.", 
                "It is a female-like small floating humanoid creature...",
                "Her white dress and navy blue beret complements her face.",
                "She feels not of this world..."]
        monologue(text) 
        quick_text("???: Hello, I am Genesis, your artificial intelligence created to guide you in The Realm.")
        type_text("You see particles appearing from thin air to form a transluscent screen.")
        text = ["Genesis: This screen is known as the [MENU]",
                "Genesis: You can access it anytime by typing 'menu' or 'm'.",
                "Genesis: And I assure you, this the [MENU] will be important!",
                "Genesis: I will provide you with helpful information and support throughout your journey.",
                "Genesis: I will reside within the MENU, and will help you in whatever path you take.",
                "Genesis: But first, lets get you familiar on how to summon the MENU.",
                "Genesis: Try opening the MENU now."]
        quick_monologue(text)
        time.sleep(0.5)
        while True:
            x = question_input("Type 'menu' or 'm' to open the MENU: ").strip().lower()
            if x == 'menu' or x == 'm':
                clear()
                quick_text("╔═══════ PLAYER MENU ═══════╗")
                quick_text("Stats (s), Inventory (i), Craft (c), PAU (p), Location (l), Back (b), Quit (q): ")
                break
            else:
                type_text("Invalid input. Please try again.")
                input_to_continue()
                clear()
                continue
        
        time.sleep(0.5)
        input_to_continue()
        clear()
        text = ["Genesis: Great! You have successfully opened the MENU.",
                "Genesis: To access what the menu has to offer, simply input the corresponding letter.",
                "Genesis: Now, might I recommend for us to get out of this forest and find a safer place to rest.", 
                "Genesis: In The Realm, danger is pretty much everywhere in the wilderness, so be cautious.",
                f"Genesis: Let us get moving... {character["Name"]}."]
        quick_monologue(text)
        input_to_continue()
        loading()

    elif decision == 'no' or decision == 'n':
        text = ["You decide to stay put.",
                "But nothing happens."]
        monologue(text)
        starting_forest_zone_1()
    else:
        type_text("Invalid option.")
        input_to_continue
        starting_forest_zone_1()

    type_text("The clearing leads to a path deeper into the forest.")
    text = ["Genesis: This area is known as Zone 1 of the Starting Forest.",
            "Genesis: Each area is divided into zones, which are sections of a location.",
            "Genesis: And each zone is divided further into individual encounters."
            "Genesis: Zones often contain enemies, resources, and rare items for you to undertake.",
            "Genesis: Let us proceed cautiously."]
    quick_monologue(text)
    while True:
        x = question_input("Proceed into Zone 1? (p): ").strip().lower()
        if x == 'menu' or x == 'm':
            menu()
            continue
        elif x == 'p':
            type_text(f"You proceed deeper into {list(zones.keys())[0]}, {zones['Starting Forest'][0]}.")
            time.sleep(1.5)
            break
        else:
            type_text("Invalid option.")
            continue
    clear()

    type_text("You enter the clearing.")
    encounter("Mossling")
    encounter_text("Genesis: All right, we have encountered our first enemy: the Mossling.")
    encounter_text("Genesis: Every time we encounter an enemy,")
    encounter_text("Genesis: we will enter a battle sequence where you will have to fight the enemy.")
    encounter_text("Genesis: In addition, I will provide you with a stat analysis of the enemy every turn.")
    encounter_text("Genesis: This will help you strategize and plan your moves accordingly.")
    encounter_text("Genesis: For example...")
    dot_effect("Booting up enemy analysis module")
    time.sleep(0.5)
    battle_stat_analyze()
    encounter_text("Genesis: You have the first move!")
    encounter_text("Genesis: Most living creatures can use a Sefirot, so ordinary physical attacks are meaningless.")
    encounter_text("Genesis: But that shouldn't be a problem for you.")
    encounter_text("Genesis: You can attack by channeling a Sefirot using your mana.")
    encounter_text("Genesis: This Mossling seems like the perfect test. Shall we?")
    i = question_input("Input any key to use your mana and channel a Sefirot: ")
    dot_effect("")
    text = ["You throw your hands out towards the Mossling...",
            "But nothing happens."]
    monologue(text)
    text = ["Genesis seems confused.",
            "Genesis: W-w-wha...",
            "Genesis: But that is impossible!",
            "Genesis: I sense the mana within you...",
            "Genesis: It should be enough to channel even the lowest of Sefirots...",
            "Genesis: Oh no! Watch out!"]
    quick_monologue(text)
    time.sleep(0.5)
    encounter_text("The Mossling, realizing the opportunity, channels its own mana and attacks you!")
    time.sleep(0.5)
    x = random.choice(list(enemy_moves["Mossling"].keys()))
    encounter_text(f"The Mossling uses {x}!")
    time.sleep(0.5)
    Health = character["Health"]
    Health -= enemy_moves["Mossling"][f"{x}"]["Damage"]
    encounter_text(f"You take {enemy_moves['Mossling'][f'{x}']['Damage']} damage!") 
    encounter_text(f"Your Health: {Health} / 100")
    input_to_continue()
    type_text("You stumble back, clutching your side where the Mossling struck you.")
    quick_text("Genesis: Are you all right?")
    a = question_input("Are you okay? Yes (y), No (n): ")
    if a == 'y' or a == 'yes':
        encounter_text("You nod, trying to shake off the pain.")
    elif a == 'n' or a == 'no':
        encounter_text("You shake your head, feeling weak from the attack.")
    else:
        encounter_text("Unable to respond properly, you simply nod.")

    encounter_text("Genesis: We need to flee! You are in no condition to fight!")
    b = question_input("Flee from the Mossling? Yes (y), No (n): ")
    if b == 'y' or b == 'yes':
        encounter_text("You try to run, but the Mossling blocks your path!")
    elif b == 'n' or b == 'no':
        encounter_text("You decide to stay and fight, despite your injuries.")
    else:
        encounter_text("Unable to respond properly, you decide to stay and fight.")
    
    time.sleep(1.8)
    encounter_text("The Mossling, realizing your hesitation, prepares to lunge at you again!")
    encounter_text("Genesis: Brace yourself!")
    text = ["You close your eyes and cover your body, preparing for the impact...",
            "But instead of pain, you feel a twinge of energy from your core.",
            "You slowly open your eyes. The Mossling senses something and stops in its tracks."]
    monologue(text)
    text = ["Genesis: Incredible... Is this what they meant for you?",
            "Genesis: It seems like you have awakened a power within yourself.",
            "Genesis: I believe this is what is called a 'Skill'..."]
    quick_monologue(text)
    text = ["You see the Mossling running towards you, ready to strike.",
            "You focus your newfound energy and prepare to counterattack.",
            "Something within you finds the words to describe this power..."]
    monologue(text)
    dot_effect("(in a faint whisper)")
    gibtext("Astral Convergence")
    time.sleep(1.5)
    character["Skill"]= "Astral Convergence {EX}"
    battle(["Mossling"])
    input_to_continue()
    clear()
    type_text("Genesis: That power...")
    quick_text("What was that? (a)")
    quick_text("Can you explain what just happened? (b)")
    quick_text("Awesome, isn't it? (c)")
    x = question_input(">>> ").strip().lower()
    clear_last_line()
    clear_last_line()
    clear_last_line()
    clear_last_line()
    if x == "a":
        quick_text("You: What was that?")
    elif x == "b":
        quick_text("You: Can you explain what just happened?")
    elif x == "c":
        quick_text("You: Awesome, isn't it?")
        dot_effect("Genesis: ")
        type_text("Genesis: I suppose so.")
    else: 
        type_text("You feel shocked at the events that has just occured.")
    
    text = ["Genesis: What you have just done was utilizing a skill.",
            "Genesis: That is something to take great joy in.",
            "Genesis: Skills are something that can only be possessed by humans",
            "Genesis: And they signify that one has obtained the attention or favor of one of the Gods themselves.",
            "Genesis: Either that or the human has great affinity in one or more of the Sefirots."]
    quick_monologue(text)


    x = three_choices("What are skill ranks? (a)", "So what does my skill do? (b)", "Cool. (c)")
    if x == "a":
        quick_text("You: What are skill ranks?")
        text = ["Genesis: Skill ranks? How do you know of this already?",
                "Genesis: No matter."]
        quick_monologue(text)
    elif x == "b":
        quick_text("You: So what does my skill do?")
        dot_effect("Genesis: ")
        type_text("Genesis: We will discover more about your skill as we progress.")
        type_text("Genesis: But allow me to explain the possibilites that your skill may have.")

    elif x == "c":
        quick_text("You: Cool.")
        dot_effect("Genesis: ")
        type_text("Genesis: Allow me to explain the possibilites that your skill may have.")
    else:
        quick_text("You stay silent.")
    
    text = ["Genesis: Each skill has a rank depending on how rare or powerful the skill is.",
            "Genesis: The ranks goes as follows:",
            "Genesis: F (lowest)",
            "Genesis: D (below average)",
            "Genesis: C (average)",
            "Genesis: B (above average)",
            "Genesis: A (rare)",
            "Genesis: S (extremely rare)"
            "Genesis: Keep in mind that EVERY human has only ONE skill.",                
            "Genesis: Humans are blessed with a skill on their sixteenth birthday.",
            "Genesis: Skill ranks are usually measured through a device known as the 'Sefirot Channel'."
            "Genesis: Alternatively, ranks can be estimated through direct testing in combat and usage.",
            "Genesis: As well as comparing it to the rarity of the skill relative to the known pool of skills.",
            "Genesis: Since you don't possess a 'Sefirot Channel', let us just estimate the power of your skill through combat.",
            "Genesis: But before we proceed...",
            "Genesis: What do you believe your rank is?"]
    quick_monologue(text)
    x = three_choices("{EX} Rank (a)", "Around S to B Rank (b)", "Probably C, D, or F (c)")
    if x == "a":
        quick_text("You: {EX} Rank")
        type_text("Genesis: What is a... {EX} rank? Nevermind then...")
    elif x == "b":
        quick_text("You: Around S to B Rank")
        type_text("Genesis: I see...")
    elif x == "c":
        quick_text("You: Probably C, D, or F")
        type_text("Genesis: Don't be too pessimistic.")
    else:
        quick_text("You shrug. Genesis seems a bit disappointed.")
    
    text = ["Genesis: In any case, if you are up for it,",
            "Genesis: Let us proceed forward.",
            "Genesis: In order to do that, allow me to inform you on how zones are structured.",
            "Genesis: Zones are mapped out by areas in the world map.",
            "Genesis: And each zone's certain area are made up of tiny little squares,",
            "Genesis: that combined together makes up a zone.",
            "Genesis: Thus, the intelligent species of The Realm has created a coordinate system,",
            "Genesis: in order to map out everything in the world.",
            "Genesis: Currently, we are at coordinates {-967, 10}"]
    quick_monologue(text)

    x = three_choices("Intelligent species? (a)", "How big is the world? (b)", "Which coordinates are we trying to get to? (c)")
    if x == "a":
        text = ["Genesis: Yes. Sorry if that tripped you up.",
                "Genesis: The Realm contains only two types of intelligent species.",
                "Genesis: Humans and Gods."]
        quick_monologue(text)
    elif x == "b":
        text = ["Genesis: I unfortunately don't know that.",
                "Genesis: The Realm is so vast,"
                "Genesis: and is full of territorial deities,"
                "Genesis: that there is no complete map of it..."]
        quick_monologue(text)
    elif x == "c":
        text = ["Genesis: Currently, we should be making our way out of the Starting Forest.",
                "Genesis: So we should try and find the coordinates marking the end of Zone 1."]
        quick_monologue(text)
    else:
        quick_text("You nod your head.")
    time.sleep(0.4)

    text = ["Genesis: Alright then, let us move onwards...",
            "Genesis: Through Starting Forest's Zone 1..."]
    input_to_continue()
    character["Coordinates"] = [-967, 10]
    loading()


# gameplay
def sfz1():
    global character
    while True:
        clear()
        coordinates, selected_item = sfz1_tile()
        character["Been There"].append(coordinates)
        clear()
        text = random.choice([f"You move to coordinates {character['Coordinates']}.",
                           f"You head towards coordinates {character['Coordinates']}.",
                           f"You find yourself at coordinates {character['Coordinates']}.",
                           f"You arrive at coordinates {character['Coordinates']}.",
                           f"You step into coordinates {character['Coordinates']}."])
        quick_text(text)

# All the coordinates
        if coordinates == [-967, 10]:
            type_text("You find yourself at the remains of a recent battle.")
            if selected_item == "'Forest Key' {Epic}":
                sfz1_coords.append([-968, 10])
                type_text("The forest reveals a hidden door to your west.")
                type_text("The door feels ominous, as if there is a huge presence behind the door.")
                input_to_continue()
                clear()
                continue
            elif selected_item == None:
                type_text("Your senses tell you that there are no monsters nearby.")
                input_to_continue()
                clear()
                continue
            elif selected_item != "'Forest Key' {Epic}":
                x = random.choice([f"The item {selected_item} did nothing."],
                              [f"The item {selected_item} had to effect on your surroundings or yourself."],
                              f"The item {selected_item} produced no effect.")
                type_text(x)
                input_to_continue()
                continue

        elif coordinates == [-967, 11]:
            if not character["Chest"]["Chest_1"]:
                while True:
                    text = ["You discover a chest, half-buried in dust. It appears to be unopened.",
                            "What do you do?"]
                    monologue(text)
                    x = question_input("Open the chest (a), Ignore it (anything else): ").strip().lower()
                    if x == "a":
                        clear()
                        quick_text("╔═══════ CHEST Open ═══════╗")
                        chest_loot = {"'Leather' {Common}": 100, "'Iron' {Uncommon}": 50, 
                                        "'Leather Armor' {Common}": 20, "'Scrap Armor' {Common}": 20, 
                                        "'Iron Dagger' {Uncommon}": 5, "'Stone Hammer' {Common}": 5, "'Stone Sword' {Common}": 5, "'Stone Shield' {Common}": 5,
                                        "'Mana Dust' {Epic}": 3, "'Mana Essence' {Legendary}": 1}
                        for loot in chest_loot:
                            chance = chest_loot[loot] / (100 - character["Luck"] * 0.5)
                            roll = random.random()
                            if roll <= chance:
                                character["Inventory"].append(loot)
                                rarity(chance, loot)
                        character["Inventory"] = rarity_sort(character["Inventory"])
                        character["Chest"]["Chest_1"] = True
                        input_to_continue()
                        break
                    elif x == "m" or x == "menu":
                        menu()
                        continue
                    else:
                        clear()
                        type_text("You ignore the chest.")
                        input_to_continue()
                        clear()
                        break
                continue

            elif selected_item == None:
                type_text("You spot an opened chest.")
                type_text("Your senses tell you that there are no monsters nearby.")
                input_to_continue()
                clear()
                continue

            else:
                x = random.choice([f"The item {selected_item} did nothing."],
                              [f"The item {selected_item} had to effect on your surroundings or yourself."],
                              f"The item {selected_item} produced no effect.")
                type_text(x)
                input_to_continue()
                continue

        elif coordinates == [-967, 12]:
            if not character["Lore"]["Lore_1"]:
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
                        character["Inventory"].append("'Houlester's Guide to the 10 Sefirots' {DAMAGED}")
                        character["Lore"]["Lore_1"] = True
                        character["Inventory"] = rarity_sort(character["Inventory"])
                    elif x == "m" or x == "menu":
                        menu()
                        continue
                    else:
                        clear()
                        type_text("You have decided to ignore the book.")
                        input_to_continue()
                        break
                continue
            elif selected_item == "'Forest Key' {Epic}":
                clear()
                text = ["The forest reveals a mysterious farm to the north.",
                        "As ominous as this farm seems, you don't feel any danger from it."]
                monologue(text)
                sfz1_coords.append([-967, 13])
                input_to_continue()
                continue
            elif selected_item == None:
                clear()
                type_text("You find yourself in a slightly more swampy area of the forest.")
                type_text("You find nothing of value or notice around you.")
                input_to_continue()
                clear()
                continue
            else:
                x = random.choice([f"The item {selected_item} did nothing."],
                              [f"The item {selected_item} had to effect on your surroundings or yourself."],
                              f"The item {selected_item} produced no effect.")
                type_text(x)
                input_to_continue()
                continue

        elif coordinates == [-966, 12]:
            if not character["Shrines"]["armageddon_shrine"]:
                while True:
                    text = ["You discover an shrine made of blackstone.",
                            "The shrine seems untounched by both man and nature.",
                            "What do you do?"]
                    quick_monologue(text)
                    x = question_input("Approach the shrine (a), Ignore it (anything else): ").strip().lower()
                    if x == "a":
                        clear()
                        text = ["You approach the shrine.",
                                "Genesis: Oh? This shrine is made for an Emperor.",
                                "Genesis: Although I don't know which Emperor this is for..."]
                        quick_monologue(text)
                        x = three_choices("What are Emperors? (a)", "What are shrines used for? (b)", "I wanna break the shrine. (c)")
                        if x == "a":
                            text = ["Genesis: Emperors are humans but with power that rivals the Gods.",
                                    "Genesis: Eventually, all that power went to their head,"
                                    "Genesis: and they rallied up and tried to take the Promised Land from the Gods."
                                    "Genesis: However, they were drove to near-extinction due to the Promised War.",
                                    "Genesis: But now, the Gods and humans live peacefully,",
                                    "Genesis: With a new generation of Emperors being cultivated."]
                            quick_monologue(text)
                        elif x == "b":
                            text = ["Genesis: Shrines are practically trophies made for Emperors.",
                                    "Genesis: Whenever a human reaches the level of an Emperor,", 
                                    "Genesis: they receive a shrine to commend their achievement of becoming an Emperor."]
                            quick_monologue(text)
                        elif x == "c":
                            text = ["Genesis: I wouldn't recommend that.",
                                    "Genesis: Even if an Emperor is dead,", 
                                    "Genesis: the destruction of their shrine may have consequences..."]
                            quick_monologue(text)
                            x = question_input("Break Shrine (a), Leave (b): ").strip().lower()
                            if x == "a":
                                clear()
                                dot_effect("BREAKING SHRINE")
                                clear()
                                type_text("You feel an ominous presence nearby.")
                                type_text("You look around but don't find anyone.")
                                character["Shrines"]["armageddon_shrine"] = True
                            elif x == "b":
                                clear()
                                type_text("You leave the shrine alone.")
                                input_to_continue()
                                continue
                            
                        else:
                            type_text("You nod and then ignore the shrine.")
                            input_to_continue()
                            continue
                        
                    elif x == "m" or x == "menu":
                        menu()
                        continue
                    else:
                        clear()
                        type_text("You decide to ignore the shrine.")
                        input_to_continue()
                        clear()
                        break
                continue
                        
            elif selected_item == None:
                type_text("You gaze upon a blackstone shrine that has been broken.")
                type_text("A sudden chill runs down your back.")
                type_text("You look around to find nothing.")
                input_to_continue()
                clear()
                continue  

            else:
                x = random.choice([f"The item {selected_item} did nothing."],
                              [f"The item {selected_item} had to effect on your surroundings or yourself."],
                              f"The item {selected_item} produced no effect.")
                type_text(x)
                input_to_continue()
                continue

        elif coordinates == [-966, 11]:
            chance = random.random()
            if selected_item != None:
                x = random.choice([f"The item {selected_item} did nothing."],
                              [f"The item {selected_item} had to effect on your surroundings or yourself."],
                              f"The item {selected_item} produced no effect.")
                type_text(x)
                input_to_continue()
                continue
            elif chance > 0.5:
                type_text("You sense an enemy nearby...")
                input_to_continue()
                clear()
                monster = random.choice([["Pebblekin"], ["Mossling"]])
                battle(monster)
                continue
            else:
                type_text("You come across a flat clearing.")
                type_text("However, your senses tells you that an enemy may be nearby.")
                input_to_continue()
                continue

        elif coordinates == [-966, 10]:
            if selected_item != None:
                x = random.choice([f"The item {selected_item} did nothing."],
                              [f"The item {selected_item} had to effect on your surroundings or yourself."],
                              f"The item {selected_item} produced no effect.")
                type_text(x)
                input_to_continue()
                continue
            while True:
                type_text("There is a wrecked wooden house nearby.")
                decision = question_input("Go inside the house (a), Ignore it (anything else): ").strip().lower()
                if decision == "a":
                    clear()
                    if not character["Lore"]["Lore_2"]:
                        text = ["You walk towards the wrecked wooden house.",
                                    "Stumbling over its remains, you find a dusty journal on the ground.",
                                    "It seems heavily weathered by the elements.",
                                    "What do you do?"]
                        monologue(text)
                        x = question_input("Pick up the journal (a), Ignore it (anything else): ").strip().lower()
                        if x == "a":
                            clear()
                            type_text("You picked up the journal and put it in your inventory.")
                            character["Inventory"].append("'Jess' Journal' {DAMAGED}")
                            character["Inventory"] = rarity_sort(character["Inventory"])
                        else:
                            type_text("You decide to ignore the journal")
                            type_text("You walk back outside.")
                            input_to_continue()
                            break
                    else:
                        type_text("You look around inside the house to find nothing.")
                        type_text("You walk back outside.")
                        input_to_continue()
                        break
                elif decision == "m" or decision == "menu":
                    menu()
                    continue
                else:
                    type_text("You decide to ignore the house.")
                    input_to_continue()
                    break   
            continue

        elif coordinates == [-965, 10]:
            fourth_emperor_list = ["'Mana Dust' {Epic}", "'Mana Essence' {Legendary}", "'Mana Core' {Mythic}"]
            chance = random.random()
            if selected_item in fourth_emperor_list:
                text = ["???: Oh... Interesting.",
                        f"???: A {selected_item}? Haven't seen any of those in a while...",
                        "???: Traveler, I have taken a great interest in you.",
                        "???: I am located in a cave south of where you are now.",
                        "???: I'll clear the forest for a path to my cave if you wish to visit."
                        "???: It would be a great pleasure to meet you."]
                monologue(text)
                sfz1_coords.append([-965, 9])
                input_to_continue()
                continue
            elif selected_item != None:
                x = random.choice([f"The item {selected_item} did nothing.",
                              f"The item {selected_item} had to effect on your surroundings or yourself.",
                              f"The item {selected_item} produced no effect."])
                type_text(x)
                input_to_continue()
                continue

            elif chance > 0.5:
                type_text("You sense an enemy nearby...")
                input_to_continue()
                clear()
                enemy = random.choice([["Forest Wisp"], ["Mossling"]])
                battle(enemy)
                continue
                
            else:
                type_text("You come across a flat clearing.")
                type_text("However, your senses tells you that an enemy may be nearby.")
                input_to_continue()
                continue

        elif coordinates == [-965, 11]:
            if selected_item != None:
                x = random.choice([f"The item {selected_item} did nothing."],
                              [f"The item {selected_item} had to effect on your surroundings or yourself."],
                              f"The item {selected_item} produced no effect.")
                type_text(x)
                input_to_continue()
                continue
            while True:
                if not character["Corpse"]["Corpse_1"]:
                    text = ["You discover a human skeleton wearing armor.",
                            "It doesn't seem to move.",
                            "What do you do?"]
                    monologue(text)
                    x = question_input("Loot the skeleton (a), Ignore it (anything else): ").strip().lower()
                    if x == "a":
                        clear()
                        quick_text("╔═══════ LOOT ═══════╗")
                        quick_text("COMMON FIND! You received a 'Scrap Armor' {Common}")
                        character["Inventory"].append("'Scrap Armor' {Common}")
                        character["Inventory"] = rarity_sort(character["Inventory"])
                        character["Corpse"]["Corpse_1"] = True
                        input_to_continue()
                        clear()
                        break
                    elif x == "m" or x == "menu":
                        menu()
                        continue
                    else:
                        type_text("You decide to ignore the skeleton.")
                        input_to_continue()
                        clear()
                        break
                else:
                    type_text("You find a skeleton with no armor.")
                    input_to_continue()
                    clear()
                    break
            continue

        elif coordinates == [-965, 12]:
            if not character["End_of_Zone"]["sfz1"]:
                battle(["Rock Golem"])
                clear()
                while True:
                    type_text("You have came to the end of Starting Forest's Zone 1.")
                    decision = question_input("Proceed to Zone 2 (p), Stay (anything else)").strip().lower()
                    if decision == "p":
                        return None
                    elif decision == "m" or decision == "menu":
                        menu()
                        continue
                    else:
                        type_text("You have decided to remain in Starting Forest's Zone 1.")
                        input_to_continue()
                        break
                continue

            elif selected_item == "'Forest Key' {Epic}":
                text = ["The forest reveals a clearing to the east.",
                        "Glancing at the clearing, you see something like an altar."]
                monologue(text)
                sfz1_coords.append([-964, 12])
                input_to_continue()
                continue

            elif selected_item != "'Forest Key' {Epic}":
                x = random.choice([f"The item {selected_item} did nothing."],
                              [f"The item {selected_item} had to effect on your surroundings or yourself."],
                              f"The item {selected_item} produced no effect.")
                type_text(x)
                input_to_continue()
                continue
                        
            else:
                while True:
                    clear()
                    type_text("You have came to the end of Starting Forest's Zone 1.")
                    decision = question_input("Proceed to Zone 2 (p), Stay (anything else)").strip().lower()
                    if decision == "p":
                        character["Location"] = "Starting Forest Zone 2"
                        return None
                    elif decision == "m" or decision == "menu":
                        menu()
                        continue
                    else:
                        type_text("You have decided to remain in Starting Forest's Zone 1.")
                        input_to_continue()
                        break
                continue

# All the secret coordinates
        elif coordinates == [-968, 10]:
            if not character["Hidden_Bosses"]["The Builder"]:
                text = ["You open the heavy door to find a torch-lit hallway.",
                        "At the end of the hallway is a humanoid figure.",
                        "Clad in a farmer's outfit, the figure seemed to be inanimate.",
                        "You approach the figure...",
                        "Slowly..."]
                monologue(text)
                custom_text("Slowly...", 0.06)
                custom_text("Slowly...", 0.04)
                custom_text("Slowly...", 0.02)
                time.sleep(1)
                clear()
                time.sleep(1)
                text = ["???: Jess? Is that you?",
                        "You recoil as the figure lifts their face up to you."]
                monologue(text)
                quick_text("???: YOU!!")
                quick_text("YOU ARE NOT JESS")
                time.sleep(1)
                battle(["The Builder"])
                clear()
                text = ["You land your final blow on The Builder.",
                        "As The Builder stumbles to his knees, he looks up resentfully at you.",
                        "The Builder looks at his hands, only to see it turn to dust as his life comes to an end."
                        "The Builder: Jess..."]
                monologue(text)
                custom_text("where are you...", 0.04)
                time.sleep(0.5)
                input_to_continue()
                continue


                        
            else:
                while True:
                    clear()
                    type_text("You find yourself in a torch-lit hallway.")
                    type_text("A pile of dust remains in the center.")
                    input_to_continue()
                    continue
            
        elif coordinates == [-967, 13]:
            if not character["Sponsor_Offer"]["The Farmer"]:
                text = ["You walk into the farm... if you could even call it one.",
                        "Around you, the remains of wooden fences and farming materials are scattered.",
                        "???: Jess?",
                        "A voice behind you makes you turn around to find something like a farmer ghost.",
                        "Farmer Ghost: Ahh... You are not Jess."]
                monologue(text)
                x = three_choices("Hell naw. (a)", "Who are you? (b)", "AHIEFHIHGIGH (c)")
                if x == "a":
                    quick_text("You: Hell naw.")
                    text = ["Farmer Ghost: Hell... naw?",
                            "Farmer Ghost: Bahh! What slang is that?"]
                    quick_monologue(text)
                elif x == "b":
                    quick_text("You: Who are you?")
                    text = ["Farmer Ghost: I am a person who died in this very field.",
                            "Farmer Ghost: I once had a family, a life here in this forest.",
                            "Farmer Ghost: But now... It is all gon-",
                            "Genesis: Blah blah blah.",
                            "Farmer Ghost: Uh... Excuse m-",
                            "Genesis: Blah blah blah."
                            "Genesis: I don't want to hear your sob story."]
                    quick_monologue(text)
                elif x == "c":
                    quick_text("You: AHIEFHIHGIGH")
                    text = ["Farmer Ghost: Ah. I must have frightened you.",
                            "Farmer Ghost: My deepest apologies.",
                            "Farmer Ghost: I'll be wandering back around now I guess..."]
                else:
                    type_text("You stare at the ghost. Unflinching.")
                
            
                text = ["Farmer Ghost: Whatever... I guess it's nice to see a living face after years...",
                            "Farmer Ghost: Say what.",
                            "Farmer Ghost: I don't have much to do.",
                            "Farmer Ghost: I have no purpose here. I lost my family. My home. Everything.",
                            "Farmer Ghost: So why don't I become your sponsor? One time offer! For FREE!"]
                quick_monologue(text)
                time.sleep(0.5)
                print("")
                type_text("You look at Genesis for an explanation.")
                text = ["Genesis: Sigh...",
                        "Genesis: When a person with a strong-enough will passes away,",
                        "Genesis: their unconsciousness turns into a ghost-like state, such as this farmer.",
                        "Genesis: We call these extremely rare ghosts 'Sponsors'.",
                        "Genesis: And these Sponsors have a special attribute."
                        "Genesis: Sponsors can then give up their power to a living being,",
                        "Genesis: something like a inheritance of some sort.",
                        "Genesis: Thus, they are valued highly.",
                        "Genesis: Sponsors also usually ask for something in exchange for their power.",
                        "Genesis: But it seems like this Sponsor is offering his power for free."
                        "Genesis: So if you want, you can inherit the power of this Sponsor.",
                        "Genesis: Although, you are restricted to only one Sponsor, so be careful!"]
                quick_monologue(text)
                type_text("You nod, and return your gaze back at the Farmer Ghost.")
                character["Sponsor_Offer"]["The Farmer"] = True
                decision = question_input("Accept Sponsor (a), Reject Sponsor (anything else): ").strip().lower()
                if decision == "a":
                    clear()
                    character["Sponsor"] = "The Farmer"
                    type_text("You have accepted [The Farmer] as your Sponsor.")
                    type_text("The Farmer dissipates, as you feel yourself getting stronger.")
                    character["Defense"] += 200
                    character["Mana"] += 400
                    character["Dodge"] += 10
                    character["Luck"] -= 5
                    character["Stat Inheritance"] += 0.01
                    type_text("As a result of your new sponsor, your stats have been reconfigured.")
                    input_to_continue()
                    continue
                else:
                    clear()
                    type_text("You have rejected [The Farmer] as your Sponsor.")
                    quick_text("Farmer Ghost: Ah well... I wish you luck on whichever path you take...")
                    type_text("The Sponsor floats away, leaving you behind in the farm's remains.")
                    input_to_continue()
                    continue

            else:
                type_text("You find yourself in the ruins of a farm.")
                input_to_continue()
                continue
                
        elif coordinates == [-965, 9]:
            if not character["Emperors"]["Fourth"]["Encounter"]:
                text = ["The forest opens up, revealing a path down southwards.",
                        "As you walk down the path, you come across a well-sized cave.",
                        "Going inside the cave, you spot a humanoid figure inside, meditating.",
                        "The figure is wearing red, gold-trimmed robes. It seems noble in a sense."
                        "You sense that they are not dangerous."]
                monologue(text)
                quick_text(f"???: Hello... Your name is {character["Name"]}, correct?")
                x = three_choices("Yes. How did you know? (a)", "No. (b)", "Who are you? (c)")
                if x == "a":
                    text = ["You: Yes. How did you know?",
                            "???: A trade secret, traveler."]
                    quick_monologue(text)
                elif x == "b":
                    text = ["You: No.",
                            "???: Hehehe... You lie traveler.",
                            "You: No.",
                            "???: How persistent.",
                            "You: No."]
                    quick_monologue(text)
                elif x == "c":
                    quick_text("You: Who are you?")
                else:
                    type_text("You nod.")
                
                type_text("The mysterious person smiles softly.")
                text = ["???: Allow me to introduce myself.",
                        "???: I am The Fourth Emperor."]
                quick_monologue(text)
                type_text("You see Genesis' eyes go wide in disbelief.")
                text = ["Genesis: The Fourth Emperor? But it was recorded that you died in the Promised War!",
                        "The Fourth Emperor: My death was... greatly exagerrated.",
                        "The Fourth Emperor: Now I am here, in this cave, living a peaceful life.",
                        "The Fourth Emperor: You have no idea how much enlightening solitude and serenity are."]
                quick_monologue(text)
                while True:
                    x = three_choices("Attack The Fourth Emperor (a)", "Ask for Wisdom (b)", "Leave (c)")
                    if x == "a":
                        text = ["You attack the emperor, only for him to smile once more.",
                                "There is no resistance."]
                        monologue(text)
                        input_to_continue()
                        clear()
                        character["Emperors"]["Fourth"]["Death"] = True
                        x = random.choice([f"You have emerged victorious from the battle!",
                        f"You stand victorious!",
                        f"You have conquered your foes in battle!",
                        f"You have achieved victory in combat!",
                        f"You have prevailed over your enemies!"])
                        encounter_text(x)
                        enemy = "The Fourth Emperor"
                        character["Strength"] = character["Strength"] + character["Stat Inheritance"] * 10000
                        character["Defense"] = character["Defense"] + character["Stat Inheritance"] * 10000
                        character["Health"] = character["Health"] + character["Stat Inheritance"] * 10000
                        character["Mana"] = character["Mana"] + character["Stat Inheritance"] * 10000
                        x = random.choice([f"Your stat inheritance of {character['Stat Inheritance']*100}% has increased your stats from defeating the {enemy}!",
                            f"Defeating the {enemy} has granted you a stat inheritance of {character['Stat Inheritance']*100}% to your stats!",
                            f"You have gained a stat inheritance of {character['Stat Inheritance']*100}% to your stats by overcoming the {enemy}!",
                            f"Your stats have been boosted by a stat inheritance of {character['Stat Inheritance']*100}% from vanquishing the {enemy}!",
                            f"By besting the {enemy}, you have acquired a stat inheritance of {character['Stat Inheritance']*100}% to your stats!"])
                        encounter_text(x)
                        encounter_text("You have been restored back to full health and mana!")
                        input_to_continue()
                        clear()
                        type_text("You walk out of the cave.")
                        input_to_continue()
                        character["Emperors"]["Fourth"]["Encounter"] = True
                        continue
                    elif x == "b":
                        text = ["The Fourth Emperor: Alright, listen closely, I will only say this once.",
                                "The Fourth Emperor: The world loves the number 5.",
                                "You: ..."]
                        monologue(text)
                        character["Wisdom"] += 10
                        input_to_continue()
                        clear()
                        type_text("You walk out of the cave.")
                        input_to_continue()
                        character["Emperors"]["Fourth"]["Encounter"] = True
                        continue
                    elif x == "c":
                        clear()
                        type_text("You walk out of the cave.")
                        input_to_continue()
                        character["Emperors"]["Fourth"]["Encounter"] = True
                        continue

                    else:
                        clear()
                        type_text("Invalid input.")
                        input_to_continue()
                        clear()
                        continue
            else:
                type_text("You see a cave... With nobody in it.")
                input_to_continue()
                continue

        elif coordinates == [-964, 12]:
            if "'Shiny Sword' {Rare}" in character["Inventory"]:
                text = ["You enter a clearing, with an altar in the middle.",
                        "The 'Shiny Sword' {Rare} flys out of your inventory and rests itself on top of the altar.",
                        "A gleaming light covers your vision.",
                        "As the light dies down, a sword flies back into your inventory."]
                monologue(text)
                quick_text("EPIC FIND! 'Shiny Sword Alpha' {Epic}")
                character["Inventory"].remove("'Shiny Sword' {Rare}")
                character["Inventory"].append("'Shiny Sword Alpha' {Epic}")
                input_to_continue()
                continue
            else:
                type_text("The altar seems to offer no benefits but it's aesthetic appeal.")
                input_to_continue()
                continue




# intro to sfz2
def starting_forest_zone_2():

    global character
    global current_location
    loading()
    current_location = zones[0][1]
    text = ["You proceed down the Unnamed Path.",
            "There seems to be nothing but thick forest,", 
            "blocking any attempts of straying off the path.",
            "You look up at the sky, and watch its color transition from blue,",
            "to orange, dark blue, and finally black.",
            "You can't help but notice the view of innumerous stars.",
            "Looking forward, you spot something in the far distance.",
            "It seems like you will have to walk for a while..."]
    monologue[text]
    loading()

def sfz2():
    ...









        

if __name__ == "__main__":
    delete_save()
    character["Coordinates"] = [-967, 10]
    main()