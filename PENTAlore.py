import time
import random
from PENTAutilities import clear, monologue, type_text, quick_text, quick_monologue, question_input, input_to_continue, character, input_to_clear


# Add descriptions to the books
books = {"book_0": {"Name": "'Houlester's Guide to the 10 Sefirots' {DAMAGED}",
                    "Description": "A damaged book that explains pretty much everything to do about the Sefirots."},
         "book_1": {"Name": "'The Numbered Emperors' {DAMAGED}"},
         "book_2": {"Name": "'An Intensive Guide to Malkhut' {COMPLETE}"},
         "book_3": {"Name": "'The Mechanics of Buffs' {DAMAGED}"},
         "book_4": {"Name": "'Mechanisms of the Keys' {COMPLETE}"},
         "book_5": {"Name": "'Anatomy of the Hycro' {COMPLETE}"},
         "book_6": {"Name": "'The Most Iconic Weapons of The Realm' {DAMAGED}"},
         "book_7": {"Name": "'Terms & Conditions of the Duel' {DAMAGED}"}
         }


journals = {"journal_0": {"Name": "'Jess' Journal' {DAMAGED}", "Description": "A damaged journal that contains the thoughts and experiences of a person named Jess."},
            "journal_1": {"Name": "'Dr. Victor's Journal' {DAMAGED}", "Description": "A damaged journal that contains the thoughts and experiences of the doctor Victor."},
            "journal_2": {"Name": "'Dr. Lucien's Journal' {DAMAGED}", "Description": "A damaged journal that contains the thoughts and experiences of the doctor Lucien."},
            "journal_3": {"Name": "'Tobias' Journal {DAMAGED}", "Description": "A damaged journal that contains the thoughts and experiences of a person named Tobias."}}



def lore(lore_item):
    # Books
    if lore_item == "'Houlester's Guide to the 10 Sefirots' {DAMAGED}":
        book_0()
    elif lore_item == "'The Numbered Emperors' {DAMAGED}":
        book_1()
    elif lore_item == "'An Intensive Guide to Malkhut' {COMPLETE}":
        book_2()
    elif lore_item == "'The Mechanics of Buffs' {DAMAGED}":
        book_3()
    elif lore_item == "'Mechanisms of the Keys' {COMPLETE}":
        book_4()
    elif lore_item == "'Anatomy of the Hycro' {COMPLETE}":
        book_5()
    elif lore_item == "'The Most Iconic Weapons of The Realm' {DAMAGED}":
        book_6()
    elif lore_item == "'Terms & Conditions of the Duel' {DAMAGED}":
        book_7()

    # Journals
    elif lore_item == "'Jess' Journal' {DAMAGED}":
        journal_0()
    elif lore_item == "'Dr. Victor's Journal' {DAMAGED}":
        journal_1()
    elif lore_item == "'Dr. Lucien's Journal' {DAMAGED}":
        journal_2()
    elif lore_item == "'Tobias' Journal' {DAMAGED}":
        journal_3()


def chapter_completion(book_number, chapter_number):
    global character
    if chapter_number in character["Book Completions"][book_number]:
        character["Book Completions"][book_number].remove(chapter_number)
    else:
        pass


def check_book(book_number):
    global character
    if len(character["Book Completions"][book_number]) == 0:
        text = ["Congratulations!",
                f"You have completed the book: {books[book_number]}",
                "You wisdom has increased!"]
        monologue(text)
        character["Wisdom"] += 55
        
        if book_number == 'book_0':
            type_text("You feel some of your sefirot affinities rising.")
            character["Malkhut"] += 1
            character["Chokmah"] += 1
            input_to_clear()
            return

        elif book_number == 'book_1':
            ...



    else:
        pass



def book_0():
    global character
    book_number = "book_0"
    while True:
        clear()
        check_book(book_number)
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
            chapter_completion(book_number, 1)
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
            chapter_completion(book_number, 1)
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
            chapter_completion(book_number, 1)
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
            chapter_completion(book_number, 1)
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
            chapter_completion(book_number, 1)
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

def book_1():
    global character
    book_number = 'book_1'
    while True:
        clear()
        check_book(book_number)
        x = ["╔═══════ BOOK 'The Numbered Emperors' {DAMAGED} ═══════╗",
             "Unreadable Parts",
             "Chapter 4: The Fourth Emperor",
             "Unreadable Parts",
             "Chapter 7: Myths and Legends",
             "Back (b)"]
        quick_monologue(x)
        print("")
        x = question_input("Which Chapter would you like to read? ").strip().lower()
        if x == "4":
            clear()
            text = ["Chapter 4: The Fourth Emperor",
                    "The Fourth Emperor is the most peaceful of the Emperors.",
                    "He is the only Emperor who has never been involved in any wars,",
                    "and is known for his love of nature and animals.",
                    "He is also the only Emperor who has never been seen by the public.",
                    "The Fourth Emperor is said to have a deep connection with the forest.",
                    "Yet, for some reason, he is also regarded as one of the more powerful Emperors."]
            monologue(text)
            print("")
            type_text("The rest of the chapter is unreadable.")
            input_to_continue()
            chapter_completion(book_number, 4)
            continue
        elif x == "7":
            clear()
            text = ["Chapter 7: Myths and Legends",
                    "There are many myths and legends about the Emperors.",
                    "One of the most popular myths is that the Emperors were once humans who ascended to godhood.",
                    "Something that, while theoretically possible, is highly unlikely.",
                    "There are also many legends about the powers of the Emperors,",
                    "and how they can control nature and manipulate reality itself through the Sefirots on a higher scale than ordinary humans.",
                    "Rivalling the Gods themselves in some cases.",
                    "It was told in stories that the first Emperor was..."]
            monologue(text)
            print("")
            type_text("The rest of the chapter is unreadable.")
            input_to_continue()
            chapter_completion(book_number, 7)
            continue
        elif x == "b":
            break
        else:
            type_text("Invalid input.")
            input_to_continue()
            continue

# Do these next, finish the books, add the functions chapter_completion and check_book
def book_2():
    while True:
        clear()
        x = ["╔═══════ BOOK 'An Intensive Guide to Malkhut' {COMPLETE} ═══════╗",
             "Chapter 1: The Basics of Malkhut",
             "Chapter 2: The Power of Malkhut",
             "Chapter 3: Malkhut and the Other Sefirots",
             "Chapter 4: Malkhut and the World",
             "Chapter 5: Deories & Spekulations"]

        quick_monologue(x)



def book_3():
    while True:
        clear()
        x = ["╔═══════ BOOK 'The Mechanics of Buffs' {DAMAGED} ═══════╗",
                        "Chapter 1: What are Buffs?",
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
            ...


def book_4():
    ...

def book_5():
    ...

def book_6():
    ...

def book_7():
    ...


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
                    "At least Dad started a farm in the northwest part of the forest."]
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


def journal_1():
    while True:
        clear()


def journal_2():
    while True:
        clear()


def journal_3():
    while True:
        clear()

