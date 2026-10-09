import random

# Generates a number from 1 to 1000 (inclusive)
randomNum = random.randint(1, 1000)
tries = 1
win = False

while tries <= 10:
    print(f'try number {tries}')
    guess = int(input('Guess a number: '))
    tries += 1

    if guess < randomNum:
        print('Number is higher')
    elif guess > randomNum:
        print('Number is lower')
    else:
        print('You win')
        win = True
        break

if not win:
    print('You lose')
    print(f'The number was: {randomNum}')