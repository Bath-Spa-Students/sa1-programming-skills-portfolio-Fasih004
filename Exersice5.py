#Create a dictionary that maps the month number to the number of days in that month
days_in_a_month = {
    1: 31,  # January
    2: 28,  # February (leap year not considered)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

#Ask the user to input the month number

month = int(input("Enter the month number (1-12): "))

if month in days_in_a_month:
    print(f"The number of days in month {month} is {days_in_a_month[month]}.")
else:
    print("Invalid month number Please enter a number between 1 and 12.")

#Advanced Requirement Task
#Ask the user if it is a leap year
#If it is a leap year, update the number of days in February to 29
#If it is not a leap year, keep the number of days in February as 28
days_in_a_month = {
    1: 31,  # January
    2: 28,  # February (leap year is considered)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

month = int(input("Enter the month number (1-12): "))

if month in days_in_a_month:
    if month == 2:  
        leap_year = input("Is it a leap year? (yes/no): ").lower()
        if leap_year == "yes":
            days_in_a_month[2] = 29 
    print(f"The number of days in month {month} is {days_in_a_month[month]}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")