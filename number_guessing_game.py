import random

while True:
    choice = input('do you want to guess the number ? (y/n): ').lower()

    if choice == 'y':
        number = random.randint(1, 10)
        guess = int(input('guess a number between 1 and 10: '))
        if guess == number:
            print('Congratulations! You guessed it right.')
        else:
            print(f'Sorry, the correct number was {number}.')
    elif choice == 'n':
        print('Thanks for playing')
        break
    else:
        print('invalid command')
