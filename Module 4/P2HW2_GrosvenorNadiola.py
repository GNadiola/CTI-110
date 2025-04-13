# Nadiola Grosvenor
# 04/12/2025
# P2HW2
# creating lists

# Module questions
module_1 = float(input("Please enter your grade for Module 1: "))
module_2 = float(input("Please enter your grade for Module 2: "))
module_3 = float(input("Please enter your grade for Module 3: "))
module_4 = float(input("Please enter your grade for Module 4: "))
module_5 = float(input("Please enter your grade for Module 5: "))
module_6 = float(input("Please enter your grade for Module 6: "))

# List
module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]

# List order output
print("---------Results---------")
print("Lowest Grade:    ", min(module_grades))
print("Highest Grade:   ", max(module_grades))
print("Sum of Grades:   ", sum(module_grades))
print("Average:         ", f'{sum(module_grades)/len(module_grades):.2f}')
print("-------------------------")
