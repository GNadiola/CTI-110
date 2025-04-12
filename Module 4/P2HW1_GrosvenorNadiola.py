# Nadiola Grosvenor
# 04/07/2025
# P1HW2
# Travel Plans

#Ask user to enter values
budget = int(input("Please enter your budget: "))
destination = str(input("Please enter your travel destination: "))
gas = int(input("Please enter the amount that will be spent on gas: "))
accomodation = int(input("Please enter the amount that will be spent on accomodations: "))
food = int(input("Please enter the amount that will be spent on food: "))

#Calculations
expenses = gas + accomodation + food
cost = budget - expenses
print("\n")

#Output
print("--------Travel Expenses--------")
print("\n")

print("Location: ", destination)
print("Initial Budget: ", budget)
print("\n")

print("Fuel: ", f'{gas:.2f}')
print("Accomodation: ", accomodation)
print("Food: ", food)
print("\n")

print("Remaining Balance: ", cost)
print("-------------------------------")