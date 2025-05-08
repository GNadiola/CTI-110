# Nadiola Grosvenor
# 4/27/2025
# P4Lab2
# Use of loops, functions and module import to complete assignments

import random

#definitions

amount_owed = round(random.uniform(0.01,100.00), 2)
print(f"You owe: ${amount_owed:.2f}")
money_in = float(input("How much cash will you put in the self-checkout?"))
change = money_in - amount_owed

def disperse_change(change):
    dollars = change // 1
    coins = (change * 100) - (dollars * 100)
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
            
def main():
        #Get amount owed
     
     

     #money for machine
     

        #change owed
     if change < 0:
        print("No Change")

     else: 
        print(f"Change Owed: ${change:.2f}")

main()