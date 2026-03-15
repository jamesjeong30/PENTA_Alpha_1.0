from PENTAutilities import tick_buffs, apply_buff, remove_buff, battle_menu, b_character_create, input_to_continue, gibtext, clear_last_line, type_text, quick_text, question_input, loading, monologue, clear, encounter_text, death, encounter
from PENTAutilities import malkhut_decision, yesod_decision, hod_decision, netzach_decision
from PENTAutilities import character, enemies, bosses, buffs, debuffs
from PENTAutilities import enemy_moves, malkhut_moves, yesod_moves, hod_moves, netzach_moves
from PENTAmusic import AudioManager
from PENTAitems import get_loot, menu
from PENTAitems import weapons, armor, items
import time
import copy
import sys
import random
import os

# Sefirot Data
sefirot_links = []

battle_enemy_stat_list = []

def battle_stat_analyze():
    for x in battle_enemy_stat_list:
        name = x["Name"]
        encounter_text(f"Genesis: Analyzing {name} stats...")
        input_to_continue
        clear()
        for stat, value in x.items():
            if stat == "Name" or stat == "Affinity":
                encounter_text(f" - {stat}: {value}")
            else:
                encounter_text(f" - {stat}: {value} / {enemies[name][stat]}")
    input_to_continue()



# chance calculations for each sefirot
def Malkhut(mana_cost):
    return True

def Yesod(mana_cost):
    dividor = 2000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 100.0001:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False
        
def Hod(mana_cost):
    dividor = 2000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 100.0001:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False
        
def Netzach(mana_cost):
    dividor = 2000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 100.0001:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False

def Tiferet(mana_cost):
    dividor = 5000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 500:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False

def Chesed(mana_cost):
    dividor = 5000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 500:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False

def Gevurah(mana_cost):
    dividor = 5000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 500:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False

def Chokmah(mana_cost):
    dividor = 10000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 1000:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False

def Binah(mana_cost):
    dividor = 15000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 1000:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False
        
def Keter(mana_cost):
    dividor = 25000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 1500:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False

def Eloki(mana_cost):
    dividor = 1000000
    chance = (mana_cost + 55.55 * character["Luck"]) / dividor
    if character["Strength"] < 3000:
        return False
    elif chance >= 1:
        return True
    else:
        roll = random.random()
        if roll <= chance:
            return True
        else:
            return False

def linkage(mana_cost, battle_character):
    global sefirot_links
    sefirot_links = []

    if Malkhut(mana_cost):
        x = random.choice([f"The powers of Kingship flows through you.",
                          f"You feel the might of Kingship within you.",
                          f"The essence of Kingship empowers you.",
                          f"You are imbued with the strength of Kingship.",
                          f"The force of Kingship surges through your veins.",
                          f"The spirit of Kingship fills your being.",
                          f"You are enveloped by the aura of Kingship.",
                          f"The energy of Kingship courses through your body.",
                          f"You feel the dominion of Kingship over you.",
                          f"The majesty of Kingship resonates within you."])
        encounter_text(x)
        sefirot_links.append("Malkhut (m)")
        input_to_continue()

    elif Yesod(mana_cost):
        x = random.choice([f"The powers of Foundation flows through you.",
                          f"You feel the stability of Foundation within you.",
                          f"The essence of Foundation empowers you.",
                          f"You are imbued with the strength of Foundation.",
                          f"The force of Foundation surges through your veins.",
                          f"The spirit of Foundation fills your being.",
                          f"You are enveloped by the aura of Foundation.",
                          f"The energy of Foundation courses through your body.",
                          f"You feel the support of Foundation over you.",
                          f"The reliability of Foundation resonates within you."])
        encounter_text(x)
        encounter_text("Astral Convergence has temporarily increased your health by 50%.")
        battle_character["Health"] = battle_character["Health"] * 1.5
        sefirot_links.append("Yesod (y)")
        input_to_continue()


    elif Hod(mana_cost):
        x = random.choice([f"The powers of Glory flows through you.",
                          f"The brilliance of Glory shines within you.",
                          f"You feel the radiance of Glory empowering you.",
                          f"The splendor of Glory fills your being.",
                          f"You are illuminated by the aura of Glory.",
                          f"The luster of Glory courses through your body.",
                          f"You feel the magnificence of Glory over you.",
                          f"The grandeur of Glory resonates within you.",
                          f"You are dazzled by the energy of Glory.",
                          f"The dazzle of Glory surges through your veins.",
                          f"You are bathed in the light of Glory."])
        encounter_text(x)
        encounter_text("Astral Convergence has temporarily increased your remaning mana by 50%.")
        battle_character["Mana"] = battle_character["Mana"] * 1.5
        sefirot_links.append("Hod (h)")
        input_to_continue()


    elif Netzach(mana_cost):
        x = random.choice([f"The powers of Eternity flows through you.",
                            f"You feel the endurance of Eternity within you.",
                            f"The essence of Eternity empowers you.",
                            f"You are imbued with the strength of Eternity.",
                            f"The force of Eternity surges through your veins.",
                            f"The spirit of Eternity fills your being.",
                            f"You are enveloped by the aura of Eternity.",
                            f"The energy of Eternity courses through your body.",
                            f"You feel the perpetuity of Eternity over you.",
                            f"The infinity of Eternity resonates within you.",
                            f"You are sustained by the power of Eternity.",
                            f"The victory of Eternity surges through your veins.",
                            f"You feel triumphant with the might of Eternity."])
        encounter_text(x)
        encounter_text("Astral Convergence has temporarily increased your strength by 50%.")
        battle_character["Strength"] = battle_character["Strength"] * 1.5
        sefirot_links.append("Netzach (n)")
        input_to_continue()


    elif Tiferet(mana_cost):
        if Yesod(mana_cost) or Hod(mana_cost) or Netzach(mana_cost):
            if character["Strength"] >= 500:
                x = random.choice([f"The powers of Beauty flows through you.",
                                  f"The radiance of Beauty illuminates your soul.",
                                  f"You are filled with the grace of Beauty.",
                                  f"The harmony of Beauty resonates within you.",
                                  f"You feel the elegance of Beauty surrounding you.",
                                  f"The beauty of Beauty enhances your being.",
                                  f"You are bathed in the glow of Beauty.",
                                  f"The splendor of Beauty fills your spirit.",
                                  f"You are surrounded by the aura of Beauty.",
                                  f"The charm of Beauty captivates your senses.",
                                  f"You feel the allure of Beauty empowering you.",
                                  f"The magnificence of Beauty uplifts your soul.",
                                  f"You are embraced by the essence of Beauty."])
                encounter_text(x)
                encounter_text("Astral Convergence has temporarily increased your remaining mana by 50%.")
                battle_character["Mana"] = battle_character["Mana"] * 1.5
                sefirot_links.append("Tiferet (t)")
                input_to_continue()


    elif Chesed(mana_cost):
        if Yesod(mana_cost) or Hod(mana_cost) or Netzach(mana_cost):
            if character["Strength"] >= 500:
                x = random.choice([f"The powers of Kindness flows through you.",
                                  f"The radiance of Kindness illuminates your soul.",
                                  f"You are filled with the grace of Kindness.",
                                  f"The harmony of Kindness resonates within you.",
                                  f"You feel the elegance of Kindness surrounding you.",
                                  f"The kindness of Kindness enhances your being.",
                                  f"You are bathed in the glow of Kindness.",
                                  f"The splendor of Kindness fills your spirit.",
                                  f"You are surrounded by the aura of Kindness.",
                                  f"The charm of Kindness captivates your senses.",
                                  f"You feel the allure of Kindness empowering you.",
                                  f"The magnificence of Kindness uplifts your soul.",
                                  f"You are embraced by the essence of Kindness."])
                encounter_text(x)
                encounter_text("Astral Convergence has temporarily increased your health by 50%.")
                battle_character["Health"] = battle_character["Health"] * 1.5
                sefirot_links.append("Chesed (c)")
                input_to_continue()


    elif Gevurah(mana_cost):
        if Yesod(mana_cost) or Hod(mana_cost) or Netzach(mana_cost):
            if character["Strength"] >= 500:
                x = random.choice([f"The powers of Severity flows through you.",
                                  f"The radiance of Severity illuminates your soul.",
                                  f"You are filled with the grace of Severity.",
                                  f"The harmony of Severity resonates within you.",
                                  f"You feel the elegance of Severity surrounding you.",
                                  f"The severity of Severity enhances your being.",
                                  f"You are bathed in the glow of Severity.",
                                  f"The splendor of Severity fills your spirit.",
                                  f"You are surrounded by the aura of Severity.",
                                  f"The charm of Severity captivates your senses.",
                                  f"You feel the allure of Severity empowering you.",
                                  f"The magnificence of Severity uplifts your soul.",
                                  f"You are embraced by the essence of Severity."])
                encounter_text(x)
                encounter_text("Astral Convergence has temporarily increased your strength by 50%.")
                battle_character["Strength"] = battle_character["Strength"] * 1.5
                sefirot_links.append("Gevurah (g)")
                input_to_continue()
    

    elif Chokmah(mana_cost):
        if Tiferet(mana_cost) or Chesed(mana_cost) or Gevurah(mana_cost):
            if character["Strength"] >= 1000:
                x = random.choice([f"The powers of Wisdom flows through you.",
                                  f"The radiance of Wisdom illuminates your soul.",
                                  f"You are filled with the grace of Wisdom.",
                                  f"The harmony of Wisdom resonates within you.",
                                  f"You feel the elegance of Wisdom surrounding you.",
                                  f"The wisdom of Wisdom enhances your being.",
                                  f"You are bathed in the glow of Wisdom.",
                                  f"The splendor of Wisdom fills your spirit.",
                                  f"You are surrounded by the aura of Wisdom.",
                                  f"The charm of Wisdom captivates your senses.",
                                  f"You feel the allure of Wisdom empowering you.",
                                  f"The magnificence of Wisdom uplifts your soul.",
                                  f"You are embraced by the essence of Wisdom."])
                encounter_text(x)
                encounter_text("Astral Convergence has temporarily increased your remaining mana by 100%")
                battle_character["Mana"] = battle_character["Mana"] * 2
                sefirot_links.append("Chokmah (hok)")
                input_to_continue()
        

    elif Binah(mana_cost):
        if Tiferet(mana_cost) or Chesed(mana_cost) or Gevurah(mana_cost):
            if character["Strength"] >= 1000:
                x = random.choice([f"The powers of Understanding flows through you.",
                                  f"The radiance of Understanding illuminates your soul.",
                                  f"You are filled with the grace of Understanding.",
                                  f"The harmony of Understanding resonates within you.",
                                  f"You feel the elegance of Understanding surrounding you.",
                                  f"The understanding of Understanding enhances your being.",
                                  f"You are bathed in the glow of Understanding.",
                                  f"The splendor of Understanding fills your spirit.",
                                  f"You are surrounded by the aura of Understanding.",
                                  f"The charm of Understanding captivates your senses.",
                                  f"You feel the allure of Understanding empowering you.",
                                  f"The magnificence of Understanding uplifts your soul.",
                                  f"You are embraced by the essence of Understanding."])
                encounter_text(x)
                encounter_text("Astral Convergence has temporarily increased your remaining mana by 100%")
                battle_character["Health"] = battle_character["Mana"] * 2
                sefirot_links.append("Binah (b)")
                input_to_continue()
        

    elif Keter(mana_cost):
        if Tiferet(mana_cost) or Chesed(mana_cost) or Gevurah(mana_cost):
            if character["Strength"] >= 1500:
                x = random.choice([f"The powers of the Crown flows through you.",
                                  f"The radiance of the Crown illuminates your soul.",
                                  f"You are filled with the grace of the Crown.",
                                  f"The harmony of the Crown resonates within you.",
                                  f"You feel the elegance of the Crown surrounding you.",
                                  f"The crown of the Crown enhances your being.",
                                  f"You are bathed in the glow of the Crown.",
                                  f"The splendor of the Crown fills your spirit.",
                                  f"You are surrounded by the aura of the Crown.",
                                  f"The charm of the Crown captivates your senses.",
                                  f"You feel the allure of the Crown empowering you.",
                                  f"The magnificence of the Crown uplifts your soul.",
                                  f"You are embraced by the essence of the Crown.",
                                  f"You feel like a true sovereign among mortals."])
                encounter_text(x)
                encounter_text("Astral Convergence has temporarily increased your strength and health by 100%")
                battle_character["Strength"] = battle_character["Strength"] * 2
                battle_character["Health"] = battle_character["Health"] * 2
                sefirot_links.append("Keter (k)")
                input_to_continue()
        

    elif Eloki(mana_cost):
        if Keter(mana_cost):
            if character["Strength"] >= 3000:
                encounter_text("The powers of Divinity flows through you.")
                encounter_text("You have surpassed the limits of the Sefirots.")
                encounter_text("Wield the ultimate power temporarily bestowed upon you.")
                encounter_text("Astral Convergence temporarily increased your strength and mana incomparably.")
                battle_character["Strength"] = battle_character["Strength"] * 55555
                battle_character["Mana"] = battle_character["Mana"] * 55555
                sefirot_links.append("Eloki (elo)")
                input_to_continue()
    
    type_text("Astral Convergence complete.")
    return battle_character





def astral_convergence(battle_character):
    clear()
    a = question_input("Input any key to activate the {EX} rank skill {Astral Convergence}: ")
    gibtext("The Tree of Life appears above you,")
    if character["Mana"] > 3000:
        gibtext("all ten Sefirot nodes radiating with immense power.")
    elif character["Mana"] > 2000:
        gibtext("all ten Sefirot nodes glowing moderately.")
    elif character["Mana"] > 1000:
        gibtext("some of the Sefirot nodes flickering faintly.")
    else:
        gibtext("with all ten Sefirot nodes dim and barely visible.")
    gibtext("'May the stars align, and let the Blessing of the Gods be with you.'")
    gibtext("Astral Convergence has been activated.")
    encounter_text(f"You have {battle_character["Mana"]} mana available.")
    
    while True:
        x = random.choice([f"How much mana would you like to invest into Astral Convergence? (Enter a number): ",
                          f"State the amount of mana you wish to channel into Astral Convergence (Enter a number): ",
                            f"Specify the mana you intend to allocate to Astral Convergence (Enter a number): ",
                            f"Indicate the mana you plan to dedicate to Astral Convergence (Enter a number): ",
                            f"Declare the mana you aim to commit to Astral Convergence (Enter a number): "])
        
        mana_usage = question_input(x)
        
        try:
            mana_usage = int(mana_usage)
        except ValueError:
            x = random.choice([f"That is not a valid amount of mana.",
                              f"Please provide a numeric value for mana.",
                              f"Mana must be expressed as a number.",
                              f"That input does not correspond to a valid mana amount.",
                              f"Enter a numerical figure for mana.",
                              f"The mana value you provided is invalid.",
                              f"Mana should be indicated using numbers only.",
                              f"That is not an acceptable mana quantity.",
                              f"Please input a valid number for mana.",
                              f"The mana amount must be a number."])
            encounter_text(x)
            encounter_text("Genesis: Astral Convergence is reactivating...")
            continue
        else:
            if int(mana_usage) == 0:
                x = random.choice([f"You have invested no mana.",
                                   f"No mana was utilized.",
                                   f"You choose to restrict the possibilities.",
                                   f"No mana was used.",
                                   f"You have used no mana on Astral Convergence"])
                encounter_text(x)
                break
            elif 0 < int(mana_usage) <= battle_character["Mana"]:
                mana_usage = int(mana_usage)
                battle_character["Mana"] -= mana_usage
                break
            elif int(mana_usage) > battle_character["Mana"]:
                x = random.choice([f"You do not have that much mana.",
                                  f"Your mana reserves cannot support that amount.",
                                  f"You lack sufficient mana for that request.",
                                  f"That amount exceeds your current mana.",
                                  f"You cannot allocate that much mana.",
                                  f"Your mana is insufficient.",
                                  f"You are unable to commit that much mana.",
                                  f"That exceeds your available mana.",
                                  f"You do not possess that amount of mana.",
                                  f"Your mana pool cannot accommodate that request."])
                encounter_text(x)
                encounter_text("Genesis: Astral Convergence is reactivating...")
                continue
            else:
                encounter_text("Genesis: Let us not fool around.")
                encounter_text("Genesis: Astral Convergence is reactivating...")
                continue
    
    time.sleep(1.5)
    x = random.choice([f"You feel a connection to the realm of infinite space...",
                      f"A surge of cosmic energy courses through you...",
                      f"You are enveloped in a radiant aura of celestial light...",
                      f"The very fabric of the universe seems to resonate with your being...",
                      f"You feel a profound link to the stars above...",
                      f"A wave of astral energy washes over you...",
                      f"You are filled with a sense of boundless potential...",
                      f"The cosmos itself seems to respond to your presence...",
                      f"You feel the power of the universe flowing through you...",
                      f"A celestial force surrounds you, empowering your very soul..."])
    encounter_text(x)
    time.sleep(0.5)
    battle_character = linkage(mana_usage, battle_character)
    time.sleep(0.5)
    gibtext("The Tree of Life fades away...")
    encounter_text(f"You have {battle_character["Mana"]} mana remaining.")
    print("")
    return battle_character




def player_turn(battle_character):
    global battle_enemy_stat_list
    global sefirot_links
    
    battle_character = astral_convergence(battle_character)

    if "Malkhut (m)" in sefirot_links:
        malkhut_moves_keys = list(malkhut_moves.keys())
        random.shuffle(malkhut_moves_keys)
        malkhut_move_list = []
        malkhut_move_list = malkhut_moves_keys[:5]
        sefirot_links.append("m")
        sefirot_links.append("malkhut")
        sefirot_links.append("mal")

    elif "Yesod (y)" in sefirot_links:
        yesod_moves_keys = list(yesod_moves.keys())
        random.shuffle(yesod_moves_keys)
        yesod_move_list = []
        yesod_move_list = yesod_moves_keys[:5]
        sefirot_links.append("y")
        sefirot_links.append("yesod")
        sefirot_links.append("yes")
    
    elif "Hod (h)" in sefirot_links:
        hod_moves_keys = list(hod_moves.keys())
        random.shuffle(hod_moves_keys)
        hod_move_list = []
        hod_move_list = hod_moves_keys[:5]
        sefirot_links.append("h")
        sefirot_links.append("hod")

    elif "Netzach (n)" in sefirot_links:
        netzach_moves_keys = list(netzach_moves.keys())
        random.shuffle(netzach_moves_keys)
        netzach_move_list = []
        netzach_move_list = netzach_moves_keys[:5]
        sefirot_links.append("n")
        sefirot_links.append("net")
        sefirot_links.append("netzach")



    while True:
        encounter_text("Sefirot Links Active:")
        print("")
        if "malkhut" in sefirot_links:
            encounter_text("Malkhut (m)")
        elif "yesod" in sefirot_links:
            encounter_text("Yesod (y)")
        elif "hod" in sefirot_links:
            encounter_text("Hod (h)")
        elif "netzach" in sefirot_links:
            encounter_text("Netzach (n)")


        sefirot_decision = question_input("Choose your Sefirot: ").strip().lower()
        
        if sefirot_decision == "menu":
            x = battle_menu(battle_character)
            clear()
            continue
        elif sefirot_decision == "e" or sefirot_decision == "enemies" or sefirot_decision == "enemy" or sefirot_decision == "a" or sefirot_decision == "analyze" or sefirot_decision == "stat" or sefirot_decision == "stat analyze" or sefirot_decision == "stats":
            battle_stat_analyze()
            continue
        elif sefirot_decision == "buff" or sefirot_decision == "buffs" or sefirot_decision == "b":
            while True:
                clear()
                temp_list = []
                encounter_text("╔═════════ ACTIVE BUFFS ═════════╗")
                for buff in range(len(list(battle_character["Buffs"].keys()))):
                    encounter_text(f"{buff + 1}. {list(battle_character['Buffs'].keys())[buff]} - {battle_character['Buffs'][buff]['Remaining']} turns remaining")
                    temp_list.append(list(battle_character['Buffs'].keys())[buff])
                encounter_text(f"B. Back [b]")
                if len(battle_character["Buffs"]) == 0:
                    x = random.choice([f"You have no buffs active.",
                                    f"No buffs have been applied",
                                    f"There are no buffs applied.",
                                    f"You have no buffs.",
                                    f"No applied buffs."])
                    encounter_text(x)
                    input_to_continue()
                    clear()
                    continue
                buff_decision = question_input("Retrive Info (#): ").strip().lower()
                if buff_decision == "b" or buff_decision == "back":
                    break
                try:
                    buff_decision = int(buff_decision)
                except ValueError:
                    x = random.choice([f"That is not a valid buff number.",
                                    f"Please select a valid buff number.",
                                    f"That buff does not exist.",
                                    f"Enter a number corresponding to a buff."])
                    encounter_text(x)
                    input_to_continue()
                    clear()
                    continue
                else:
                    if 1 <= buff_decision <= len(temp_list):
                        buff_choice = temp_list[buff_decision - 1]
                        clear()
                        encounter_text(f"╔══════ {buff_choice}'s Effects ══════╗")
                        for stat, value in battle_character["Buffs"][buff_choice].items():
                            encounter_text(f" - {stat}: {value}")
                        input_to_continue()
                        clear()
                        continue
                    else:
                        x = random.choice([f"That is not a valid buff number.",
                                        f"Please select a valid buff number.",
                                        f"That buff does not exist.",
                                        f"Enter a number corresponding to a buff."])
                        encounter_text(x)
                        input_to_continue()
                        clear()
                        continue

        

        elif sefirot_decision not in sefirot_links:
            x = random.choice([f"You have not linked to that Sefirot.",
                              f"That Sefirot is not currently linked.",
                              f"You cannot access that Sefirot at this time.",
                              f"That Sefirot link is inactive.",
                              f"You are not connected to that Sefirot."])
            encounter_text(x)
            input_to_continue()
            clear()
            continue
    

        elif sefirot_decision == "m" or sefirot_decision == "malkhut" or sefirot_decision == "mal":
            clear()
            order = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            temp_list = []
            x = "1"
            quick_text("╔═════════ Available Malkhut Moves ═════════╗")
            for number_ig in order:
                for move_malkhut in malkhut_move_list:
                    if move_malkhut.split("[")[1].split("]")[0] == number_ig:
                        temp_list.append(move_malkhut)
                        quick_text(f"{x}. {move_malkhut.split('[')[0].strip()}")
                        x = str(int(x) + 1)
            quick_text(f"B. Back [b]")
            move_choice, damage, move_type, battle_character = malkhut_decision(temp_list, battle_character)
            clear()
            
            if move_choice == "back" or move_choice == None:
                continue
            elif move_choice == "menu":
                x = battle_menu(battle_character)
                clear()
                continue
            elif move_choice == "e" or move_choice == "enemies" or move_choice == "enemy" or move_choice == "a" or move_choice == "analyze" or move_choice == "stat" or move_choice == "stat analyze" or move_choice == "stats":
                battle_stat_analyze()
                clear()
                continue
            elif move_choice == "buff" or move_choice == "buffs" or move_choice == "b":
                clear()
                encounter_text("Active Buffs")
                for buff in range(len(character["Buffs"])):
                    encounter_text(f"{buff + 1}. {character['Buffs'][buff]['Name']} - {character['Buffs'][buff]['Remaining']} turns remaining")
                if len(character["Buffs"]) == 0:
                    x = random.choice([f"You have no buffs active.",
                                      f"No buffs have been applied",
                                      f"There are no buffs applied.",
                                      f"You have no buffs.",
                                      f"No applied buffs."])
                    encounter_text(x)
                input_to_continue()
                clear()
                continue
            elif move_type == "single":
                while True:
                    for enemy in range(len(battle_enemy_stat_list)):
                        encounter_text(f"{enemy + 1}. {battle_enemy_stat_list[enemy]['Name']} - {battle_enemy_stat_list[enemy]['Health']} HP")
                    target_decision = question_input("Which enemy would you like to target (#), Back (b): ").strip().lower()
                    if target_decision == "b" or target_decision == "back":
                        encounter_text("You have powered down your attack.")
                        encounter_text("Returning to Sefirot selection...")
                        break
                    try:
                        target_decision = int(target_decision)
                    except ValueError:
                        x = random.choice([f"That is not a valid enemy number.",
                                        f"Please select a valid enemy number.",
                                        f"That enemy does not exist.",
                                        f"Enter a number corresponding to an enemy."])
                        encounter_text(x)
                    else: 
                        if 1 <= target_decision <= len(battle_enemy_stat_list):
                            attack_decision = target_decision - 1
                            break
                        else:
                            x = random.choice([f"That is not a valid enemy number.",
                                            f"Please select a valid enemy number.",
                                            f"That enemy does not exist.",
                                            f"Enter a number corresponding to an enemy."])
                            encounter_text(x)
                if target_decision == "b" or target_decision == "back":
                    continue
                else:
                    break
            break


        elif sefirot_decision == "y" or sefirot_decision == "yesod" or sefirot_decision == "yes":
            clear()
            order = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            temp_list = []
            x = "1"
            quick_text("╔═════════ Available Yesod Moves ═════════╗")
            for number_ig in order:
                for move_yesod in yesod_move_list:
                    if move_yesod.split("[")[1].split("]")[0] == number_ig:
                        temp_list.append(move_yesod)
                        quick_text(f"{x}. {move_yesod.split('[')[0].strip()}")
                        x = str(int(x) + 1)
            quick_text(f"B. Back [b]")
            move_choice, damage, move_type, battle_character = yesod_decision(temp_list, battle_character)
            clear()

            if move_choice == "back" or move_choice == None:
                continue
            elif move_choice == "menu":
                x = battle_menu(battle_character)
                clear()
                continue
            elif move_choice == "e" or move_choice == "enemies" or move_choice == "enemy" or move_choice == "a" or move_choice == "analyze" or move_choice == "stat" or move_choice == "stat analyze" or move_choice == "stats":
                battle_stat_analyze()
                clear()
                continue
            elif move_choice == "buff" or move_choice == "buffs" or move_choice == "b":
                clear()
                encounter_text("Active Buffs")
                for buff in range(len(character["Buffs"])):
                    encounter_text(f"{buff + 1}. {character['Buffs'][buff]['Name']} - {character['Buffs'][buff]['Remaining']} turns remaining")
                if len(character["Buffs"]) == 0:
                    x = random.choice([f"You have no buffs active.",
                                      f"No buffs have been applied",
                                      f"There are no buffs applied.",
                                      f"You have no buffs.",
                                      f"No applied buffs."])
                    encounter_text(x)
                input_to_continue()
                clear()
                continue
            elif move_type == "single":
                while True:
                    for enemy in range(len(battle_enemy_stat_list)):
                        encounter_text(f"{enemy + 1}. {battle_enemy_stat_list[enemy]['Name']} - {battle_enemy_stat_list[enemy]['Health']} HP")
                    target_decision = question_input("Which enemy would you like to target (#), Back (b): ").strip().lower()
                    if target_decision == "b" or target_decision == "back":
                        encounter_text("You have powered down your attack.")
                        encounter_text("Returning to Sefirot selection...")
                        break
                    try:
                        target_decision = int(target_decision)
                    except ValueError:
                        x = random.choice([f"That is not a valid enemy number.",
                                        f"Please select a valid enemy number.",
                                        f"That enemy does not exist.",
                                        f"Enter a number corresponding to an enemy."])
                        encounter_text(x)
                    else: 
                        if 1 <= target_decision <= len(battle_enemy_stat_list):
                            attack_decision = target_decision - 1
                            break
                        else:
                            x = random.choice([f"That is not a valid enemy number.",
                                            f"Please select a valid enemy number.",
                                            f"That enemy does not exist.",
                                            f"Enter a number corresponding to an enemy."])
                            encounter_text(x)
                if target_decision == "b" or target_decision == "back":
                    continue
                else:
                    break
            break


        elif sefirot_decision == "h" or sefirot_decision == "hod":
            clear()
            order = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            temp_list = []
            x = "1"
            quick_text("╔═════════ Available Hod Moves ═════════╗")
            for number_ig in order:
                for move_hod in hod_move_list:
                    if move_hod.split("[")[1].split("]")[0] == number_ig:
                        temp_list.append(move_hod)
                        quick_text(f"{x}. {move_hod.split('[')[0].strip()}")
                        x = str(int(x) + 1)
            quick_text(f"B. Back [b]")
            move_choice, damage, move_type, battle_character = hod_decision(temp_list, battle_character)
            clear()

            if move_choice == "back" or move_choice == None:
                continue
            elif move_choice == "menu":
                x = battle_menu(battle_character)
                clear()
                continue
            elif move_choice == "e" or move_choice == "enemies" or move_choice == "enemy" or move_choice == "a" or move_choice == "analyze" or move_choice == "stat" or move_choice == "stat analyze" or move_choice == "stats":
                battle_stat_analyze()
                clear()
                continue
            elif move_choice == "buff" or move_choice == "buffs" or move_choice == "b":
                clear()
                encounter_text("Active Buffs")
                for buff in range(len(character["Buffs"])):
                    encounter_text(f"{buff + 1}. {character['Buffs'][buff]['Name']} - {character['Buffs'][buff]['Remaining']} turns remaining")
                if len(character["Buffs"]) == 0:
                    x = random.choice([f"You have no buffs active.",
                                      f"No buffs have been applied",
                                      f"There are no buffs applied.",
                                      f"You have no buffs.",
                                      f"No applied buffs."])
                    encounter_text(x)
                input_to_continue()
                clear()
                continue
            elif move_type == "single":
                while True:
                    for enemy in range(len(battle_enemy_stat_list)):
                        encounter_text(f"{enemy + 1}. {battle_enemy_stat_list[enemy]['Name']} - {battle_enemy_stat_list[enemy]['Health']} HP")
                    target_decision = question_input("Which enemy would you like to target (#), Back (b): ").strip().lower()
                    if target_decision == "b" or target_decision == "back":
                        encounter_text("You have powered down your attack.")
                        encounter_text("Returning to Sefirot selection...")
                        break
                    try:
                        target_decision = int(target_decision)
                    except ValueError:
                        x = random.choice([f"That is not a valid enemy number.",
                                        f"Please select a valid enemy number.",
                                        f"That enemy does not exist.",
                                        f"Enter a number corresponding to an enemy."])
                        encounter_text(x)
                    else: 
                        if 1 <= target_decision <= len(battle_enemy_stat_list):
                            attack_decision = target_decision - 1
                            break
                        else:
                            x = random.choice([f"That is not a valid enemy number.",
                                            f"Please select a valid enemy number.",
                                            f"That enemy does not exist.",
                                            f"Enter a number corresponding to an enemy."])
                            encounter_text(x)
                if target_decision == "b" or target_decision == "back":
                    continue
                else:
                    break
            break


        elif sefirot_decision == "n" or sefirot_decision == "net" or sefirot_decision == "netzach":
            clear()
            order = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            temp_list = []
            x = "1"
            quick_text("╔═════════ Available Netzach Moves ═════════╗")
            for number_ig in order:
                for move_netzach in netzach_move_list:
                    if move_netzach.split("[")[1].split("]")[0] == number_ig:
                        temp_list.append(move_netzach)
                        quick_text(f"{x}. {move_netzach.split('[')[0].strip()}")
                        x = str(int(x) + 1)
            quick_text(f"B. Back [b]")
            move_choice, damage, move_type, battle_character = netzach_decision(temp_list, battle_character)
            clear()

            if move_choice == "back" or move_choice == None:
                continue
            elif move_choice == "menu":
                x = battle_menu(battle_character)
                clear()
                continue
            elif move_choice == "e" or move_choice == "enemies" or move_choice == "enemy" or move_choice == "a" or move_choice == "analyze" or move_choice == "stat" or move_choice == "stat analyze" or move_choice == "stats":
                battle_stat_analyze()
                clear()
                continue
            elif move_choice == "buff" or move_choice == "buffs" or move_choice == "b":
                clear()
                encounter_text("Active Buffs")
                for buff in range(len(character["Buffs"])):
                    encounter_text(f"{buff + 1}. {character['Buffs'][buff]['Name']} - {character['Buffs'][buff]['Remaining']} turns remaining")
                if len(character["Buffs"]) == 0:
                    x = random.choice([f"You have no buffs active.",
                                      f"No buffs have been applied",
                                      f"There are no buffs applied.",
                                      f"You have no buffs.",
                                      f"No applied buffs."])
                    encounter_text(x)
                input_to_continue()
                clear()
                continue
            elif move_type == "single":
                while True:
                    for enemy in range(len(battle_enemy_stat_list)):
                        encounter_text(f"{enemy + 1}. {battle_enemy_stat_list[enemy]['Name']} - {battle_enemy_stat_list[enemy]['Health']} HP")
                    target_decision = question_input("Which enemy would you like to target (#), Back (b): ").strip().lower()
                    if target_decision == "b" or target_decision == "back":
                        encounter_text("You have powered down your attack.")
                        encounter_text("Returning to Sefirot selection...")
                        break
                    try:
                        target_decision = int(target_decision)
                    except ValueError:
                        x = random.choice([f"That is not a valid enemy number.",
                                        f"Please select a valid enemy number.",
                                        f"That enemy does not exist.",
                                        f"Enter a number corresponding to an enemy."])
                        encounter_text(x)
                    else: 
                        if 1 <= target_decision <= len(battle_enemy_stat_list):
                            attack_decision = target_decision - 1
                            break
                        else:
                            x = random.choice([f"That is not a valid enemy number.",
                                            f"Please select a valid enemy number.",
                                            f"That enemy does not exist.",
                                            f"Enter a number corresponding to an enemy."])
                            encounter_text(x)
                if target_decision == "b" or target_decision == "back":
                    continue
                else:
                    break
            break



    move_choice = move_choice.split('(')[0].strip()

    while True:
        if move_type == None:
            break
        
        elif "single" in move_type:
            chance = random.randint(0, 100)
            if character["Critical"] > chance:
                damage = damage * 2
                x = random.choice([f"CRITICAL! Your attack hits with devastating force!",
                                  f"CRITICAL! Your strike lands with immense power!",
                                  f"CRITICAL! Your attack is a crushing blow!",
                                  f"CRITICAL! Your strike is a powerful hit!",
                                  f"CRITICAL! Your strike is a mighty blow!"])
                encounter_text(x)
                time.sleep(0.2)
            battle_enemy_stat_list[attack_decision]["Health"] -= round(damage - battle_enemy_stat_list[attack_decision]["Defense"]/1.5)
            dealt_damage = round(damage - battle_enemy_stat_list[attack_decision]["Defense"]/1.5)
            attack_decision = battle_enemy_stat_list[attack_decision]["Name"]
            y = random.choice([f"You use {move_choice} on {attack_decision}!",
                                  f"{attack_decision} is struck by {move_choice}!",
                                  f"You unleash {move_choice} upon {attack_decision}!",
                                  f"{attack_decision} is hit with {move_choice}!",
                                  f"You cast {move_choice} targeting {attack_decision}!",
                                  f"{attack_decision} is affected by {move_choice}!",
                                  f"You activate {move_choice} against {attack_decision}!",
                                  f"{attack_decision} is impacted by {move_choice}!",
                                  f"You direct {move_choice} at {attack_decision}!"])
            encounter_text(y)
            time.sleep(0.2)
            x = random.choice([f"You deal {dealt_damage} damage to {attack_decision}!",
                                   f"{attack_decision} takes {dealt_damage} damage!",
                                   f"{attack_decision} is hit for {dealt_damage} damage!",
                                   f"You have inflicted {dealt_damage} to {attack_decision}!",
                                   f"{attack_decision} suffers {dealt_damage} damage!",
                                   f"{dealt_damage} damage dealt to {attack_decision}!",
                                   f"{attack_decision} endures {dealt_damage} damage!",
                                   f"{attack_decision} receives {dealt_damage} damage!",
                                   f"{dealt_damage} points of damage inflicted on {attack_decision}!",
                                   f"{attack_decision} is struck for {dealt_damage} damage!",
                                   f"{attack_decision} absorbs {dealt_damage} damage!",
                                   f"{dealt_damage} damage lands on {attack_decision}!",
                                   f"{attack_decision} is wounded for {dealt_damage} damage!"])
            encounter_text(x)
            input_to_continue()
            break


        elif "aoe" in move_type:
            chance = random.randint(0, 100)
            if character["Critical"] > chance:
                damage = damage * 2
                x = random.choice([f"CRITICAL! Your attack hits with devastating force!",
                                  f"CRITICAL! Your strike lands with immense power!",
                                  f"CRITICAL! Your attack is a crushing blow!",
                                  f"CRITICAL! Your strike is a powerful hit!",
                                  f"CRITICAL! Your strike is a mighty blow!"])
                encounter_text(x)
                time.sleep(0.2)
            for enemy in battle_enemy_stat_list:
                enemy["Health"] -= round(damage - enemy["Defense"]/1.5)
            

            x = random.choice([f"You use {move_choice} on all enemies!",
                              f"All enemies are struck by {move_choice}!",
                              f"You unleash {move_choice} upon all enemies!",
                              f"All enemies are hit with {move_choice}!",
                              f"You cast {move_choice} targeting all enemies!",
                              f"All enemies are affected by {move_choice}!",
                              f"You activate {move_choice} against all enemies!",
                              f"All enemies are impacted by {move_choice}!",
                              f"You direct {move_choice} at all enemies!"])
            encounter_text(x)
            time.sleep(0.2)
            for enemy in battle_enemy_stat_list:
                attack_decision = enemy["Name"]
                dealt_damage = round(damage - enemy["Defense"]/1.5)
                y = random.choice([f"You deal {dealt_damage} damage to {attack_decision}!",
                                   f"{attack_decision} takes {dealt_damage} damage!",
                                   f"{attack_decision} is hit for {dealt_damage} damage!",
                                   f"You have inflicted {dealt_damage} to {attack_decision}!",
                                   f"{attack_decision} suffers {dealt_damage} damage!",
                                   f"{dealt_damage} damage dealt to {attack_decision}!",
                                   f"{attack_decision} endures {dealt_damage} damage!",
                                   f"{attack_decision} receives {dealt_damage} damage!",
                                   f"{dealt_damage} points of damage inflicted on {attack_decision}!",
                                   f"{attack_decision} is struck for {dealt_damage} damage!",
                                   f"{attack_decision} absorbs {dealt_damage} damage!",
                                   f"{dealt_damage} damage lands on {attack_decision}!",
                                   f"{attack_decision} is wounded for {dealt_damage} damage!"])
                encounter_text(y)
            input_to_continue()
            break
        

        elif "buff" in move_type:
            x = random.choice([f"You use {move_choice} to buff yourself!",
                              f"You activate {move_choice} to enhance your abilities!",
                              f"You cast {move_choice} to strengthen your attributes!",
                              f"You invoke {move_choice} to empower yourself!",
                              f"You channel {move_choice} to boost your stats!"])
            encounter_text(x)
            input_to_continue()
            break

        elif "heal" in move_type:
            x = random.choice([f"You use {move_choice} to heal yourself to {battle_character['Health']} health!",
                              f"You activate {move_choice} to restore your health to {battle_character['Health']}!",
                              f"You cast {move_choice} to recover your health to {battle_character['Health']}!",
                              f"You invoke {move_choice} to mend your wounds to {battle_character['Health']}!",
                              f"You channel {move_choice} to rejuvenate your health to {battle_character['Health']}!"])
            encounter_text(x)
            input_to_continue()
            break

        elif "restore" in move_type:
            x = random.choice([f"You use {move_choice} to restore your mana to {battle_character['Mana']} mana!",
                              f"You activate {move_choice} to replenish your mana to {battle_character['Mana']}!",
                              f"You cast {move_choice} to recover your mana to {battle_character['Mana']}!",
                              f"You invoke {move_choice} to regain your mana to {battle_character['Mana']}!",
                              f"You channel {move_choice} to refresh your mana to {battle_character['Mana']}!"])
            encounter_text(x)
            input_to_continue()
            break


    if battle_character["Health"] <= 0:
        x = random.choice([f"You have died in battle.",
                          f"You have fallen in combat.",
                          f"You have been defeated in battle.",
                          f"You have perished in combat."]) 
        encounter_text(x)
        input_to_continue()
        death()

    for enemies_battle in battle_enemy_stat_list:
        if enemies_battle["Health"] <= 0:
            battle_enemy_stat_list.remove(enemies_battle)
            x = random.choice([f"{enemies_battle['Name']} has been vanquished!",
                          f"{enemies_battle['Name']} has been defeated!",
                          f"{enemies_battle['Name']} has been slain!",
                          f"{enemies_battle['Name']} has been overcome!",
                          f"{enemies_battle['Name']} has been bested!"])
            encounter_text(x)
            input_to_continue()


    if len(battle_enemy_stat_list) == 0:
        return "victory", battle_character
    else:
        return None, battle_character
...


def enemy_turn(battle_character):
    encounter_text("Enemy Turn:")
    for enemy in battle_enemy_stat_list:
        move_list = list(enemy_moves[enemy["Name"]].keys())
        enemy_decision = random.choice(move_list)
        if enemy_moves[enemy["Name"]][enemy_decision]["Cost"] > enemy["Mana"]:
            a = random.choice([f"{enemy["Name"]} decided to recover their mana!",
                               f"{enemy["Name"]} doesn't use a move and instead focuses on mana recovery!",
                               f"{enemy["Name"]} rests to recover mana",
                               f"{enemy["Name"]} forfeits their turn to recover mana."])
            encounter_text(a)
            enemy["Mana"] += round(enemy["Mana"] * 0.33)
        else:
            damage = enemy_moves[enemy["Name"]][enemy_decision]["Damage"]
            enemy["Mana"] -= enemy_moves[enemy["Name"]][enemy_decision]["Cost"]

            x = random.choice([f"{enemy['Name']} uses {enemy_decision} on you!",
                            f"{enemy['Name']} unleashes {enemy_decision} upon you!",
                            f"{enemy['Name']} casts {enemy_decision} targeting you!",
                            f"{enemy['Name']} activates {enemy_decision} against you!",
                            f"{enemy['Name']} directs {enemy_decision} at you!"])
            encounter_text(x)
            time.sleep(0.2)
            parry_chance = random.randint(0, 100)
            if character["Parry"] > parry_chance:
                x = random.choice([f"PARRY! You deflect {enemy['Name']}'s attack!",
                                  f"PARRY! You deflect {enemy['Name']}'s strike!",
                                  f"PARRY! You deflect {enemy['Name']}'s assault!",
                                  f"PARRY! You deflect {enemy['Name']}'s blow!",
                                  f"PARRY! You deflect {enemy['Name']}'s attack!"])
                encounter_text(x)
                time.sleep(0.2)
            else:
                dodge_chance = random.randint(0, 100)
                if character["Dodge"] > dodge_chance:
                    x = random.choice([f"DODGE! You evade {enemy['Name']}'s attack!",
                                    f"DODGE! You sidestep {enemy['Name']}'s strike!",
                                    f"DODGE! You duck under {enemy['Name']}'s assault!",
                                    f"DODGE! You avoid {enemy['Name']}'s blow!",
                                    f"DODGE! You slip past {enemy['Name']}'s attack!"])
                    encounter_text(x)
                    time.sleep(0.2)
            
            if character["Parry"] <= parry_chance and character["Dodge"] <= dodge_chance:
                battle_character["Health"] -= round(damage - battle_character["Defense"]/1.5)
                y = random.choice([f"{enemy['Name']} deals {round(damage - battle_character['Defense']/1.5)} damage to you!",
                            f"You take {round(damage - battle_character['Defense']/1.5)} damage!",
                            f"You are hit for {round(damage - battle_character['Defense']/1.5 )} damage!",
                            f"You have been inflicted {round(damage - battle_character['Defense']/1.5)} damage!",
                            f"You suffer {round(damage - battle_character['Defense']/1.5)} damage!",
                            f"{round(damage - battle_character['Defense']/1.5)} damage dealt to you!",
                            f"You endure {round(damage - battle_character['Defense']/1.5)} damage!",
                            f"You receive {round(damage - battle_character['Defense']/1.5)} damage!",
                            f"{round(damage - battle_character['Defense']/1.5)} points of damage inflicted on you!",
                            f"You are struck for {round(damage - battle_character['Defense']/1.5)} damage!",
                            f"You absorb {round(damage - battle_character['Defense']/1.5)} damage!",
                            f"{round(damage - battle_character['Defense']/1.5)} damage lands on you!",
                            f"You are wounded for {round(damage - battle_character['Defense']/1.5)} damage!"])
                encounter_text(y)
                encounter_text(f"Your Health: {battle_character['Health']} / {character['Health']}")
            elif character["Parry"] > parry_chance:
                encounter_text(f"You have dealt {round(damage/5)} damage back to {enemy['Name']} with your parry!")
                enemy["Health"] -= round(damage/5)
            elif character["Dodge"] > dodge_chance:
                encounter_text(f"You have dealt {round(damage/10)} damage back to {enemy['Name']} with your dodge!")
                enemy["Health"] -= round(damage/10)
        input_to_continue()

    for enemies_battle in battle_enemy_stat_list:
        if enemies_battle["Health"] <= 0:
            battle_enemy_stat_list.remove(enemies_battle)
            x = random.choice([f"{enemies_battle['Name']} has been vanquished!",
                          f"{enemies_battle['Name']} has been defeated!",
                          f"{enemies_battle['Name']} has been slain!",
                          f"{enemies_battle['Name']} has been overcome!",
                          f"{enemies_battle['Name']} has been bested!"])
            encounter_text(x)
            input_to_continue()

        if battle_character["Health"] <= 0:
            return "defeat", battle_character
        elif len(battle_enemy_stat_list) == 0:
                return "victory", battle_character
        else:
            return None, battle_character
        



def battle(encountered_enemies):
    global enemies
    global character
    global battle_enemy_stat_list
    for enemy in encountered_enemies:
        encounter(enemy)
    battle_character = b_character_create()
    battle_enemy_stat_list = []
    for battle_enemy in encountered_enemies:
        battle_enemy_x = copy.deepcopy(enemies[battle_enemy])
        battle_enemy_stat_list.append(battle_enemy_x)
    
    decision = question_input("Genesis: Would you like an analysis? Yes (y), No (any other input): ").strip().lower()
    if decision == "y" or decision == "yes":
        battle_stat_analyze()
    else:
        pass

    while True:
        clear()
        end, battle_character = player_turn(battle_character)
        if end == "victory":
            break

        end, battle_character = enemy_turn(battle_character)
        if end == "defeat":
            death()
        
        if battle_character["Mana"] < character["Mana"]:
            battle_character["Mana"] += battle_character["Mana Regen"]
            x = random.choice([f"You have regenerated mana over the course of the battle.",
                               f"Your mana regen stat has restored a part of your mana.",
                               f"Mana has been restored naturally.",
                               f"Your mana increased naturally.",
                               f"You absorb natural mana into your mana pool."])
            encounter_text(x)
            if battle_character["Mana"] > character["Mana"]:
                battle_character["Mana"] = character["Mana"]
        
        battle_character = tick_buffs(battle_character)

    # Victory Sequence
    x = random.choice([f"You have emerged victorious from the battle!",
                      f"You stand victorious!",
                      f"You have conquered your foes in battle!",
                      f"You have achieved victory in combat!",
                      f"You have prevailed over your enemies!"])
    encounter_text(x)

    for enemy in encountered_enemies:
        character["Strength"] = character["Strength"] + character["Stat Inheritance"] * enemies[enemy]["Strength"]
        character["Defense"] = character["Defense"] + character["Stat Inheritance"] * enemies[enemy]["Defense"]
        character["Health"] = character["Health"] + character["Stat Inheritance"] * enemies[enemy]["Health"]
        character["Mana"] = character["Mana"] + character["Stat Inheritance"] * enemies[enemy]["Mana"]
        x = random.choice([f"Your stat inheritance of {character['Stat Inheritance']*100}% has increased your stats from defeating the {enemy}!",
                          f"Defeating the {enemy} has granted you a stat inheritance of {character['Stat Inheritance']*100}% to your stats!",
                          f"You have gained a stat inheritance of {character['Stat Inheritance']*100}% to your stats by overcoming the {enemy}!",
                          f"Your stats have been boosted by a stat inheritance of {character['Stat Inheritance']*100}% from vanquishing the {enemy}!",
                          f"By besting the {enemy}, you have acquired a stat inheritance of {character['Stat Inheritance']*100}% to your stats!"])
        encounter_text(x)
    
    encounter_text("You have been restored back to full health and mana!")
    input_to_continue()

    for enemy in encountered_enemies:
        get_loot(enemy)
    
    input_to_continue()
    clear()




    
