try:
    age = int(input("Enter Age: "))
    income = int(input("Enter Income: "))
    risk = income/age
    print(f"Your Risk is {risk}")
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Age cannot be Zero")