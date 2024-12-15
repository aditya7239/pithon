weight = float(input('Enter your Weight: '))
unit = int(input('''Choose whether you want to -
(1) Kilograms to Pounds
(2) Pounds to Kilograms

Enter your choice (1 or 2): '''))

if unit == 1:
    converted = weight / 0.45
    print(f'{weight} Kilograms = {converted} Pounds')
elif unit == 2:
    converted = weight * 0.45
    print(f'{weight} Pounds = {converted} Kilograms')
else:
    print('Invalid Input')
