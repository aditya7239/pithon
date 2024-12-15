# Program to Check whether a person is Eligible for Loan or Not

salary = float(input("Enter your (Annual) Salary: "))
creditScore = float(input("Enter your Credit Score: "))
criminalRecordIn = input("Have you had any criminal records (Y/N): ")

if criminalRecordIn == "Y":
    criminalRecord = True
elif criminalRecordIn == "N":
    criminalRecord = False
else:
    print("Invalid Response")
    print("Criminal Record to be Taken Negative")
    criminalRecord = False
if salary >= 1000000:
    highSalary = True
else:
    highSalary = False

if creditScore >= 670:
    highCredit = True
else:
    highCredit = False

if highCredit and highSalary and not criminalRecord:
    print("*****-Eligible for Loan-*****")
else:
    print("*****-Not Eligible for Loan-*****")
