from PENTAutilities import tick_buffs, apply_buff, remove_buff, battle_menu, b_character_create, input_to_continue, gibtext, clear_last_line, type_text, quick_text, question_input, loading, monologue, clear, encounter_text, death, encounter
from PENTAutilities import malkhut_decision, yesod_decision, hod_decision, netzach_decision
from PENTAutilities import character, enemies, bosses, buffs, debuffs
from PENTAutilities import enemy_moves, malkhut_moves, yesod_moves, hod_moves, netzach_moves
from PENTAmusic import AudioManager
from PENTAitems import get_loot, menu
from PENTAitems import weapons, armor, items    
from PENTAbattle import astral_convergence, linkage, sefirot_links, Malkhut, Yesod, Hod, Netzach
import time
import copy
import sys
import random
import os
import threading

all_range = ["Close", "Mid", "Far", "Behind", "Side", "Above", "Below", "Conceptual"]
battle_range = "Mid"

def new_battle(encountered_enemies):
    global enemies
    global character
    global battle_enemy_stat_list
    global all_range, battle_range
    clear()
    for enemy in encountered_enemies:
        encounter(enemy)
    battle_character = b_character_create()
    battle_enemy_stat_list = []
    for battle_enemy in encountered_enemies:
        battle_enemy_x = copy.deepcopy(enemies[battle_enemy])
        battle_enemy_stat_list.append(battle_enemy_x)
    

    while True:
        # The battle itself
        battle_character = astral_convergence(battle_character)
        clear()

        break


    # Victory Sequence
    clear()
    quick_text("╔══════════════ VICTORY ══════════════╗")
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
    clear()
    
    for enemy in encountered_enemies:
        get_loot(enemy)
    
    input_to_continue()
    clear()