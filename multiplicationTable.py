# Program to print the multiplication table of a given number

# Input the number
num = int(input("Enter a number: "))

# Print the multiplication table
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
