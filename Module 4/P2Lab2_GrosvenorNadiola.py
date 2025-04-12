#1. Nadiola Grosvenor
#2. 4/12/25
#3. P2Lab2
#4. This assignment teaches the student how to create a Python program that will write code that uses a dictionary to store user input and displays output to the user

# Set up
cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

# Dictionary keys
keys = cars.keys()

print(keys)
print(*keys, sep = ", ")

# Input
car_type = input("Enter a vehicle to see its mpg:")

# mpg
car_mpg = cars[car_type]

# Output
print(f"The", car_type, "gets", car_mpg, "miles per gallon.")

# Input
miles = float(input(f"How many miles will you drive the {car_type} ?"))

# Calculate
gallons = miles/car_mpg

# Output
print(f"{gallons:.2f} gallon(s) are needed to drive the {car_type} {miles} miles.")
