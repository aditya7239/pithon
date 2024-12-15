a = int(input("Enter first Number "))
b = int(input("Enter second Number "))
c = int(input("Enter third Number "))

if a>b and a>c:
    print(f"{a} is the largest number")
elif b>c and b>a:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")