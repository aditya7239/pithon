print("Welcome to Calculator")
n1 = float(input("Enter First No: "))
# Taking input from user for first number.
n2 = float(input("Enter second Number: "))
# Taking Input From User For Second Number.
operator = str(input("Choose an Operator (+,-,*,/) :"))
if operator == "+":
    tn = n1 + n2
    print(tn)
elif operator == "-":
    tn = n1 - n2
    print(tn)
    # Printing the result of subtraction operation on two numbers entered by
elif operator == "*":
    tn = n1 * n2
    print(tn)
    # Printing The Result Of Multiplication Operation On Two Numbers Entered By User .
elif operator == "/" and n2 != 0:
    tn = float(n1 / n2)
    print("The Answer Is", tn, " ")
    # Division is not possible in Python so we use float() function here.
