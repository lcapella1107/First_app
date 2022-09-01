Hourly_rate = float(input('Please Enter your hourly rate:'))
Weekly_hours = float(input('Please enter your regular weekly hours:'))
week_pay = Hourly_rate * Weekly_hours
year_pay = week_pay * 52
user = input('Would you like to know your pay after taxes?')
if user == 'yes' or user == 'Yes' or user == 'y':
    Tax_rate = float(input('Please Enter the tax rate in your state:'))
    if Tax_rate == '%':
        Tax_rate = float(input("Please enter the tax rate without the '%' sign"))
    else:
        Year_tax = year_pay - (year_pay * (Tax_rate / 100))
        print("This is your yearly pay: " + str(year_pay))
        print("This is your yearly pay after taxes: " + str(Year_tax))
else:
     user == "no" or user == 'No' or user == 'n'
     print("This is your yearly pay: " + str(year_pay))
    #print("You're making this amount per year " + year_pay)
    #print("You're making this amount per year after taxes")