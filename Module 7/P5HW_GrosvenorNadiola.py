# Nadiola Grosvenor
# 4/27/2025
# P4Lab2
# Use of loops, functions and module import to create a program

def create_character():
    #function to create character
    name = input("Name your duck: ")
    agility = int(input(f"Enter {name}'s agility level: "))
    fighter_class = int(input(f"Enter{name}'s fighter level: "))
    stamina = int(input(f"Enter{name}'s stamina level: ")) 
    lives = 3
    character = {'Name': name, 'Agility': agility, 'Fighter Class': fighter_class, 'Stamina': stamina, 'Lives': lives }
    print(f"{name} has been created \U0001F431")
    return character

def display_characters(characters):
    #displays all characters
    print("\U+1FAB6	\U+1F338 \U+1F4AE \U+1FAB7 \U+1F41D \U+1FAB7 \U+1F4AE \U+1F338 \U+1FAB6	")
    print("~~~~~~~ALL DUCKS~~~~~~~")
    for char in characters:
        print(f"Name: {char['name']}, Agility: {char['agility']}, Fighter Class: {char['fighter_class']}, Stamina: {char['stamina']}")

def attack(attacker, defender):
    #performs attack and tells whether the character won or lost
    damage = random.randint(0, 100)
    defender

