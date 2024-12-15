ch = input("Enter a character: ")
if ch.isupper():
    print(f"{ch} is an uppercase character.")
elif ch.islower():
    print(f"{ch} is a lowercase character.")
elif ch.isdigit():
    print(f"{ch} is a digit.")
else:
    print(f"{ch} is a special character.")
