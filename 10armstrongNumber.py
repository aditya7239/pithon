number = int(input("Enter a number: "))
sum_of_cubes = sum([int(digit) ** 3 for digit in str(number)])
if number == sum_of_cubes:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
