import time
import random
from PENTAutilities import clear, monologue, type_text, quick_text, quick_monologue, question_input, input_to_continue

def lore(lore_item):
    if lore_item == "'Houlester's Guide to the 10 Sefirots' {DAMAGED}":
        book_0()
    elif lore_item == "'Jess' Journal' {DAMAGED}":
        journal_0()


def book_0():
    while True:
        clear()
        x = ["╔═══════ BOOK 'Houlester's Guide to the 10 Sefirots' {DAMAGED} ═══════╗",
                        "Chapter 1: The Sefirots",
                        "Chapter 2: Mana",
                        "Chapter 3: Malkhut",
                        "Unreadable Parts",
                        "Chapter 10: Chokmah",
                        "Unreadable Parts",
                        "Chapter 17: The Gods",
                        "Unreadable Parts",
                        "Back (b)"]
        quick_monologue(x)
        print("")
        x = question_input("Which Chapter would you like to read? ").strip().lower()
        if x == "1":
            clear()
            type_text("Chapter 1: The Sefirots")
            text = ["The Sefirots are the ten attributes in the Kabbalah, the Tree of Life.",
                    "In the Tree of Life, there is a hiearchy between the Sefirots.",
                    "At the top. Keter.",
                    "Right below Keter are Binah and Chokmah.",
                    "Then Gevurah, Tiferet, and Hesed.",
                    "The second lowest level introduces Hod, Yesod, and Netzach.",
                    "And the lowest level Sefirot: Malkhut.",
                    "Through the ten Sefirots, the Tree of Life is formed,",
                    "and through the tree, all of reality is encompassed within it.",
                    "It is also through the ten Sefirots where all aspects of consciesess and existence can be found.",
                    "Malkhut is...",]
            monologue(text)
            print("")
            type_text("The rest of the chapter is unreadable.")
            input_to_continue()
            continue
        elif x == "2":
            clear()
            type_text("Chapter 2: Mana")
            text = ["Mana is a universal power that can be found within every living thing.",
                    "Plants, animals, monsters, even you and I have mana.",
                    "It is through this mana where one is able to channel Sefirots.",
                    "The Sefirots near unreachable power sources.",
                    "Yet it is ONLY through mana where practically everyone with a sufficient mana pool,",
                    "is able to reach those powers..."]
            monologue(text)
            print("")
            type_text("The rest of the chapter is unreadable.")
            input_to_continue()
            continue
        elif x == "3":
            clear()
            type_text("Chapter 3: Malkhut")
            text = ["Malkhut means Kingdom, and is the tenth Sefirot.",
                    "It is associated with the realm of matter/earth and relates to the physical world",
                    "While some may consider Malkhut as the weakest Sefirot,",
                    "It is only through Malkhut where the other Sefirots can take physical form.",
                    "Essentially, whenever one utilizes a Sefirot besides Malkhut,",
                    "they are unconsciously using Malkhut to bring their Sefirot into the real world."]
            monologue(text)
            print("")
            type_text("The rest of the chapter is unreadable.")
            input_to_continue()
            continue
        elif x == "10":
            clear()
            type_text("Chapter 10: Chokmah")
            text = ["Chokmah means Wisdom, and is the second Sefirot.",
                    "It embodies wisdom coming from nothingness,",
                    "and represents the first power of conscious intellect and subtle manifestation.",
                    "Chokmah is one of the strongest Sefirots,",
                    "and can only be utilized by those with those of extremely high mana pools.",
                    "One thing that does seperate Chokmah from the rest is..."]
            monologue(text)
            print("")
            type_text("The rest of the chapter is unreadable.")
            input_to_continue()
            continue
        elif x == "17":
            clear()
            type_text("Chapter 17: The Gods")
            text = ["The Gods are the sole agents of the Sefirots.",
                    "They serve directly under the Sefirots,",
                    "and are thus gifted direct power from the Sefirots.",
                    "There are five main Gods..."]
            monologue(text)
            print("")
            type_text("The rest of the chapter is unreadable.")
            input_to_continue()
            continue
        elif x == "b":
            break
        elif x == "20":
            clear()
            type_text("You found a single page untouched by Mother Nature between the thick book.")
            type_text("The page has only one sentence.")
            type_text("Chapter 20: Eloki.")
            input_to_continue()
            continue
        else:
            type_text("Invalid input.")
            input_to_continue()
            continue

def journal_0():
    while True:
        clear()
        x = ["╔═══════ JOURNAL 'Jess' Journal' {DAMAGED} ═══════╗",
                        "Unreadable Parts",
                        "--- ENTRY 21 ---",
                        "Unreadable Parts",
                        "--- ENTRY 59 ---",
                        "Back (b)"]
        quick_monologue(x)
        print("")
        x = question_input("Which entry would you like to read? ").strip().lower()
        if x == "21":
            clear()
            text = ["ENTRY 21",
                    "We had to run.",
                    "That is what my parents told me.",
                    "I don't know why we had to run.",
                    "It all happened so fast.",
                    "Dad told me that the Emperors were rebelling.",
                    "Why would the Emperors do that?",
                    "Now I'm living with Mom and Dad.",
                    "All alone.",
                    "In this forest.",
                    "At least Dad started a farm nearby..."]
            monologue(text)
            print("")
            type_text("The rest of the entry is unreadable.")
            input_to_continue()
            continue
        elif x == "59":
            clear()
            text = ["WE ARE NOT ALONE",
                    "WE ARE NOT ALONE",
                    "WE ARE NOT ALO..."]
            monologue(text)
            print("")
            type_text("The rest of the entry is unreadable.")
            input_to_continue()
            continue
        elif x == "b":
            break
        elif x == "1":
            clear()
            text = ["You flip to the first page to find two words.",
                    "Haven City"]
            monologue(text)
            input_to_continue()
            continue
        else:
            type_text("Invalid input.")
            input_to_continue()
            continue


