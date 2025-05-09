# Nadiola Grosvenor
# 4/27/2025
# P4Lab2
# Use of loops, functions and module import to create a program

import random


def create_character():
    #function to create character
    name = input("Name your duck: ")
    print("Your duck's agility can range from 0 to 150." )
    agility = int(input(f"Enter {name}'s agility level: "))
    if agility > 150 or agility <0:
        print("Error")
        agility = int(input(f"Enter {name}'s agility level: "))
        
    print("There are three weapons to choose from! \n 1. Stick  2. Rock  3. Water" )
    weapon = int(input(f"Enter the number of {name}'s weapon: "))
    print("Your duck's stamina can range from 0 to 150." )
    stamina = int(input(f"Enter{name}'s stamina level: ")) 
    if stamina > 150 or stamina <0:
        print("Error")
        stamina = int(input(f"Enter {name}'s stamina level: "))
    lives = 3
    character = {'Name': name, 'Agility': agility, 'Weapon #': weapon, 'Stamina': stamina, 'Lives': lives }
    print(f"{name} has been created \U0001F431")
    return character

def display_characters(characters):
    #displays all characters
    print("\U0001FAB6	\U0001F338 \U0001F4AE \U0001FAB7 \U0001F41D \U0001FAB7 \U0001F4AE \U0001F338 \U0001FAB6	")
    print("~~~~~~~ALL DUCKS~~~~~~~")
    for char in characters:
        print(f"Name: {char['name']}, Agility: {char['agility']}, Weapon: {char['weapon']}, Stamina: {char['stamina']}, Lives:{char['lives']}")

def fighter_class_abilities(abilities):
    #displays the abilities of each fighter class
    print("\U0001FA84 \U0001FAA8 \U0001F30A")
    print("~~~~~Weapon Attacks~~~~~")
    
def attack(attacker, defender):
    #performs attack and tells whether the character won or lost
    damage = random.randint(0, 100)
    if ['weapon'] == 1:
        damage = damage * 0.5
    if ['weapon'] == 2:
        damage = damage * 3
    if ['weapon'] == 3:
        damage = damage * 2

    if damage >= 33:
        defender['lives'] -=1 
    elif damage >= 66:
        defender['lives'] -=2
    elif damage >= 99: 
        defender['lives'] -=3
    else:
        defender['lives'] = 3

    print(f"{attacker['name']} is using... ")
    if ['weapon'] == 1:
        print(f"...a rock, and tossing it weakly at {defender['name']} \U0001FAA8")
    elif ['weapon'] == 2:
        print(f"...AVADA KEDAVRA on {defender['name']}!!!")
    elif ['weapon'] == 3:
        print(f"...waterbending~ on {defender['name']}!")

    print(f"The damage done to {defender['name']} is {damage}/100!!")
    return defender ['lives']

def main():
    #options for creating character, displaying character, attacking, end game.
    #create character
    duck_1 = create_character()
    duck_2 = create_character()

    #list characters
    ducks = [duck_1, duck_2]

    #display characters
    display_characters(ducks)

    #Make an attack
    duck_1['lives'] = attack(duck_1, duck_2) 