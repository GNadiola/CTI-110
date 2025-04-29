# Nadiola Grosvenor
# 4/22/2025
# P4Lab2
# displays information to users using loops.

do_again = 'yes'

while do_again != "no":
    user_num = int(input("Enter an integer: "))

    if user_num >= 0;
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")
    
    do_again = input("Would you to run the program again? ")

print("Program is ending")