'''if, else, elif
''''''
age = int(input("Please enter your age: "))
if age>=18:
    print('You are eligible to vote')
else:
    print('Sorry you are not eligible for voting yet.')'''


total_marks = int(input("Total Marks percentage: ")) 
if total_marks>90:
    print("A grade")
elif total_marks>80 and total_marks<=90:
    print('B Grade')
else:
    print('C Grade')
