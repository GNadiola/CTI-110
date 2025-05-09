# Nadiola Grosvenor
# 5/5/2025
# P4Lab2
# Use of loops, functions and module import to create a game program

import turtle
import time
import random

"""
# Setup screen
def ducks_moving(): #using turtle to make images move
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Duck Battle!")

# get gifs
    screen.addshape("duck.gif")
    screen.addshape("duck2.gif")

# ducks 1 & 2
    duck1 = turtle.Turtle()
    duck1.shape("duck.gif")
    duck1.penup()
    duck1.goto(-200, 0)

    duck2 = turtle.Turtle()
    duck2.shape("duck2.gif")
    duck2.penup()
    duck2.goto(200, 0)

    for round in range(3):
        duck1.goto(-50, 0)
        time.sleep(0.5)
        duck1.goto(-200, 0)

        duck2.goto(50, 0)
        time.sleep(0.5)
        duck2.goto(200, 0)

    turtle.done()"""

print("Welcome to Duck Fight!\nYou will create two ducks and choose their weapons. They will then battle it out in a series of rounds!! \U0001F94A")

def create_character():
    #function to create character

    name = input("Name your duck: ")
    print("Your duck's agility can range from 0 to 15." )
    agility = int(input(f"Enter {name}'s agility level: "))
    if agility > 15 or agility <0:
        print("Error")
        agility = int(input(f"Enter your duck's agility level: "))
        
    print("There are three weapons to choose from! \n 1. Stick  2. Rock  3. Water" )
    weapon = int(input(f"Enter the number of {name}'s weapon: "))
    print("Your duck's stamina can range from 0 to 15." )
    stamina = int(input(f"Enter {name}'s stamina level: ")) 
    if stamina > 15 or stamina <0:
        print("Error")
        stamina = int(input(f"Enter {name}'s stamina level: "))
    feathers = 45
    character = {'Name': name, 'Agility': agility, 'Weapon #': weapon, 'Stamina': stamina, 'Feathers': feathers }
    print(f"{name} has been created \U0001F986")
    return character

def display_characters(characters):
    #displays all characters
    print("\U0001F986 \U0001FAB6 \U0001F338 \U0001F4AE \U0001FAB7 \U0001F41D \U0001FAB7 \U0001F4AE \U0001F338 \U0001FAB6 \U0001F986")
    print("~~~~~~~ALL DUCKS~~~~~~~")
    for char in characters:
        print(f"Name: {char['Name']}, Agility: {char['Agility']}, Weapon: {char['Weapon #']}, Stamina: {char['Stamina']}, Feathers:{char['Feathers']}")
    print("\U0001F986 \U0001F986 \U0001F986 \U0001F986 \U0001F986 \U0001F986 \U0001F986 \U0001F986 \U0001F986 \U0001F986 \U0001F986")


#def fighter_class_abilities(powers):
    #displays the abilities of each fighter class
   # print("\U0001FA84 \U0001FAA8 \U0001F30A")
    #print("~~~~~Weapon Attacks~~~~~")

def is_alive(character):
        return character['Feathers'] > 0
    
def attack(attacker, defender):
    #performs attack and tells whether the character won or lost
    damage = random.randint(0, 10)
    random_bonus = random.randint(0, 10)
    if attacker['Weapon #'] == 1:
        damage = damage * 3
    if attacker['Weapon #'] == 2:
        damage = damage * 0.5
    if attacker['Weapon #'] == 3:
        damage = damage * 2

    damage = max(0, int(damage + (attacker['Agility'] * 0.5) + (attacker['Stamina'] * 0.3) - random_bonus))  

    print(f"{attacker['Name']} is using... ", end="")
    time.sleep(2) #dramatic pause
    weapon = attacker['Weapon #']
    attack_type = random.randint(0, 3)
    if weapon == 1:
        if attack_type == 0:
         print(f"...a stick, and casts AVADA KEDAVRA on {defender['Name']}! \U0001FA84")
         damage = damage*3
        if attack_type == 1:
         print(f"...a stick, and casts an attack on {defender['Name']}! \U0001FA84")
         damage = damage*2
        if attack_type == 2:
         print(f"...a stick, and casts AVADA KEDAVRA on {defender['Name']}! \U0001FA84")
         damage = damage*3
        if attack_type == 3:
         print(f"...a stick, and casts a shrinking spell on {defender['Name']}! \U0001FA84")
         damage = damage*1
    elif weapon == 2:
        if attack_type == 0:
            print(f"...a rock, and throws a direct hit at {defender['Name']} \U0001FAA8")
            damage = damage*3
        if attack_type == 1:
            print(f"...a rock, and roughly tosses it at {defender['Name']} \U0001FAA8")
            damage = damage*2
        if attack_type == 2:
            print(f"...a rock, and throws a direct hit at {defender['Name']}! \U0001FAA8")
            damage = damage*3
        if attack_type == 3:
            print(f"...a rock, and weakly tosses it at {defender['Name']} \U0001FAA8")
            damage = damage*1
    elif weapon == 3:
        if attack_type == 0:
            print(f"...WATERBENDING on {defender['Name']}! \U0001F30A")
            damage = damage*3
        if attack_type == 1:
            print(f"...a small wave on {defender['Name']}! \U0001F30A")
            damage = damage*2
        if attack_type == 2:
            print(f"...WATERBENDING on {defender['Name']}! \U0001F30A")
            damage = damage*3
        if attack_type == 3:
            print(f"...a small splash on {defender['Name']}! \U0001F30A")
            damage = damage*1

    
    print(f"The damage done to {defender['Name']} is {damage}/45!!")
    

    if damage >= 44: 
        print(f"{attacker['Name']}'s attack was SUPER strong!!")
    elif damage >= 30:
        print(f"{attacker['Name']}'s attack was very strong!!")
    elif damage >= 15:
        print(f"{attacker['Name']}'s attack was kinda strong!")
    elif damage < 15:
        print(f"{attacker['Name']}'s attack wasn't very strong!")
    defender['Feathers'] -= damage
    if defender['Feathers'] < 0:
            defender['Feathers'] = 0
            
    print(f"{defender['Name']} now has {defender['Feathers']} feathers.")
    return defender ['Feathers']


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
    round_num = 1
    while is_alive(duck_1) and is_alive(duck_2):
        print(f"\n🔁 Round {round_num}")
        duck_2['Feathers'] = attack(duck_1, duck_2)

        if not is_alive(duck_2):
            print(f"\n💀 {duck_2['Name']} has been defeated!")
            break

        duck_1['Feathers'] = attack(duck_2, duck_1)

        if not is_alive(duck_1):
            print(f"\n💀 {duck_1['Name']} has been vanquished!")
            break
        
        #moving to next round with dramatic pause
        time.sleep(3) 
        input("Hit Enter to continue to the next round \U0001F94A")
        round_num += 1

    # Declare winner
    if duck_1['Feathers'] > 0:
        print(f"\n🏆 {duck_1['Name']} is the champion!")
    else:
        print(f"\n🏆 {duck_2['Name']} is the champion!")
    #ducks_moving()

if __name__ == "__main__":
    main()
