# Nadiola Grosvenor
# 04/07/2025
# P2HW1
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
print("Location:          ", destination)
print("Initial Budget:     $", f'{budget:.2f}')
print("Fuel:               $", f'{gas:.2f}')
print("Accomodation:       $", f'{accomodation:.2f}')
print("Food:               $", f'{food:.2f}')
print("-------------------------------")

print("\n")

print("Remaining Balance:  $", f'{cost:.2f}')