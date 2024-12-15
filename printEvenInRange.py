num1 = int(input("Enter the Lower limit of range: "))
num2 = int(input("Enter the Upper limit of range: "))

for i in range(num1, num2+1):
    if (i % 2) == 0: 
        print(i)

