n = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"The sum of even numbers from 1 to {n} is **{even_sum}**.")
print(f"The sum of odd numbers from 1 to {n} is **{odd_sum}**.")
