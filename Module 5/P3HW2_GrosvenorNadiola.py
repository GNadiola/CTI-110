# Nadiola Grosvenor
# 04/16/2025
# P3HW2
# Assesses student understanding of decision structures

# Request employee info
name = input("Enter employee name: ")
hours_worked = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter employee pay rate: "))

# Evaluate overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    over_pay = overtime_hours * (pay_rate * 1.5)
    reg_pay = 40 * pay_rate
    gross_pay = reg_pay + over_pay

else:
    over_pay = 0 
    overtime_hours = 0
    reg_pay = hours_worked * pay_rate
    gross_pay = reg_pay + over_pay

print("Employee Name: ", name, "\n")
print(" Hours Worked    Pay Rate    Overtime    Overtime Pay    RegHour Pay     Gross Pay", "\n")
print( "    ", hours_worked, "        ", pay_rate, "          ", overtime_hours,"         $", over_pay, "           $", reg_pay, "         $", gross_pay,)
