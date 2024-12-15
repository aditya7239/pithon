def sum_divisors():
    while True:
        num = input(">>>    ")
        if num == 'q':
            break
        try:
            num = int(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue

        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)

        dsum = 0
        for i in factors:
            dsum += i
        print(f"The sum of the divisors of {num} is {dsum}.")
print("Enter a number (or 'q' to quit)")
sum_divisors()
