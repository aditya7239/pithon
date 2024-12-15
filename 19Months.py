months = {
    'january': 31, 'february': 28, 'march': 31, 'april': 30,
    'may': 31, 'june': 30, 'july': 31, 'august': 31,
    'september': 30, 'october': 31, 'november': 30, 'december': 31
}
# (a)
month_name = input("Enter the month name: ").lower()
print("Number of days:", months.get(month_name, "Invalid month name"))

# (b)
print("Months in alphabetical order:", sorted(months.keys()))

# (c)
print("Months with 31 days:", [month for month, days in months.items() if days == 31])

# (d)
sorted_months = sorted(months.items(), key=lambda x: x[1])
print("Months sorted by number of days:", sorted_months)
