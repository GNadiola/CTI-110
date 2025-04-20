# Nadiola Grosvenor
# 04/19/2025
# P3Lab
# Calculating the most efficient coin count

# Enter the amount
money = float(input("Please enter the amount of money: $"))

# Calculations and Logic
dollars = money // 1
coins = (money * 100) - (dollars * 100)


# Output
print(f'{dollars:.0f}', "Dollars")
print(f'{coins:.0f}', "Coins")
