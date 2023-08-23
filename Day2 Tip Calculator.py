print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_percent2 = 1 + int(tip_percent) / 100
#print(tip_percent2)
number_of_people = input("How many people to split the bill?")
each_person_pay = ( float(total_bill) * float(tip_percent2) ) / int(number_of_people)
#print(each_person_pay)
formatted_pay = "{:.2f}".format(each_person_pay)  # Formatting the float to 2 decimal places
print("Each person should pay: $" + formatted_pay)