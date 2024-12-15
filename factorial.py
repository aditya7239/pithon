num = int(input("Enter a Number whose factorial you want"))
factorial = 1
for i in range(1,num+1):
    factorial*=i
if factorial == 0:
    factorial=1

print(f"factorial of {num} is {factorial}")