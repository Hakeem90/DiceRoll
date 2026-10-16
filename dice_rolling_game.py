import random


while True:
    choice = input('do you want to roll the dice ? (y/n): ').lower()

    if choice == 'y':
        choice2 = input('how many die do you want to roll? (1/2): ')
        print(choice2)
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1) if choice2 == '1' else print(
            f'({die1}, {die2})') if choice2 == '2' else None
    elif choice == 'n':
        print('Thanks for playing')
        break
    else:
        print('invalid command')
