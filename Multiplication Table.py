num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
