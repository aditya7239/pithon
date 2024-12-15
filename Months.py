month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# Part (a)
month = input("Enter the month name: ")
if month in month_days:
    print(f"The number of days in {month} is {month_days[month]}.")
else:
    print("Invalid month name entered.")

# Part (b)
print("The months with 31 days are:")
for month, days in month_days.items():
    if days == 31:
        print(f"{month}")
