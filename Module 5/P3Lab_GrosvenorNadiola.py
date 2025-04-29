# Nadiola Grosvenor
# 04/19/2025
# P3Lab
# Calculating the most efficient coin count

# Enter the amount
money = float(input("Please enter the amount of money: $"))

# Calculations and Logic
dollars = money // 1
coins = (money * 100) - (dollars * 100)
quarters = coins // 25
dimes = (coins - (quarters * 25)) // 10
nickels = (coins - ((quarters * 25) + (dimes * 10)))// 5
pennies = (coins - ((quarters * 25) + (dimes * 10) + (nickels * 5))) // 1

# Output (if/else statements)
if dollars >= 1:
    print(f'{dollars:.0f}', "Dollars")
if coins >= 1:
    if quarters >1:
        print(f'{quarters:.0f}', "Quarters")
    elif quarters == 1:
        print(f'{quarters:.0f}', "Quarter")
    if dimes >1:
        print(f'{dimes:.0f}', "Dimes")
    elif dimes == 1:
        print(f'{dimes:.0f}', "Dime")  
    if nickels >1:
        print(f'{nickels:.0f}', "Nickels") 
    elif nickels == 1:
        print(f'{nickels:.0f}', "Nickel") 
    if pennies >1:
        print(f'{pennies:.0f}', "Pennies")
    elif pennies == 1:
        print(f'{pennies:.0f}', "Penny")
    else: 
        print("No Change")


