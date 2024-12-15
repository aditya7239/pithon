name = input("Enter your Name: ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be less than 50 characters")
else:
    print(f"Hello {name}")