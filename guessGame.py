import random
def guessNumber(x):
    random_number=random.randint(1,x)
    guessed=0
    while guessed!=random_number:
        guessed=int(input('Guess number'))
        if guessed<random_number:
            print('too low!! try again')
        elif guessed > random_number:
            print('too high!! try again')
    print(f'wow!!! you guessed the number {random_number}')
guessNumber(500)
