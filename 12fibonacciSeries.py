terms = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b 

print()
