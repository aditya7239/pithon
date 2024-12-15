n = int(input("Enter a number: "))
sum = 0
i = int(input("eNTER FIRST TERM"))
d = int(input("Enter the common difference"))
while i <= n:
    sum += d * (n - i + 1) / 2
    i += d
print(sum)
