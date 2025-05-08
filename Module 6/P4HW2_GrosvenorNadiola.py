# Nadiola Grosvenor
# 4/27/2025
# P4Lab2
# Assesses student understanding of decision structures


name = str(input("Enter employee's name or 'Done' to terminate: "))
#loop
while name != 'done':
  
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

    name = str(input("Enter employee's name or 'Done' to terminate: "))

number_of_names = len(name)
print(number_of_names)
total_overpay = sum(over_pay)
print(total_overpay)
total_reg_pay = sum(reg_pay)
print(total_reg_pay)
total_pay = sum(gross_pay)
print(total_pay)

