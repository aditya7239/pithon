num = int(input("Enter a Number: "))
x = num
count = 0
while x > 0:
    x //= 10
    count+=1

if count==0:
    count=1

print(f"{num} has {count} digits")