import random

for i in range(1):
    secret_number = random.randint(0, 10)

i = 0  # 'i' is the number of guesses the user has made
n = 1
print('Guess a number between 1 and 10 which I am thinking About: ')
while i < 3:
    guess = int(input(f"Guess {n}: "))
    if guess == secret_number:
        print("You got it!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    i += 1
    n += 1
    if i == 3:
        print("You ran out of guesses!")