#1. Nadiola Grosvenor
#2. 4/12/25
#3. P1Lab1
#4. This assignment teaches the student how to create a Python program that will calculate the diameter, circumference, and area of a circle

#Inputting the radius
radius = float(input('What is the radius? '))

#Calculations
diameter = 2 * radius
circumference = 2 * 3.14 * radius
area = 3.14 * radius * radius

#Outputs
print("The diameter of the circle is ", f'{diameter:.1f}')
print("The circumference of the circle is ", f'{circumference:.2f}')
print("The area of the circle is ", f'{area:.3f}')