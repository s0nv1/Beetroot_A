
# Task 1
# The Guessing Game.
import random
import time

dict_ionary = {1: 'HARDCORE MODE', 2: 'Difficult but possible!', 3: 'It\'s more interesting',
               4: 'Are you a mathematician?', 5: 'omg... good luck'}


def load_game():
    print('Connecting', end='')
    for i in range(3):
        time.sleep(1)
        print('.', end='')
    time.sleep(1)
    print('\nGuess the number from 1 to 10.')
    time.sleep(1.5)


def number_of_attempts():
    print('Choose the number of attempts from 1 to 5.')
    time.sleep(1.5)
    while True:
        try:
            num = int(input('Write: '))
        except ValueError:
            print('Number selected incorrectly, enter again.')
        else:
            if num < 1 or num > 5:
                print('From 1 to 5!')
            else:
                time.sleep(1)
                print(dict_ionary[num])
                return num


def start_game(n):
    random_digit = random.randint(1, 10)
    time.sleep(1.5)
    attempt = 0
    print('Just do it!')
    time.sleep(1)
    while attempt != n:
        try:
            choosen_digit = int(input('Your choice: '))
        except ValueError:
            print('Number selected incorrectly, try again.')
        else:
            if choosen_digit < 1 or choosen_digit > 10:
                print('You only need to write from 1 to 10.')
            else:
                attempt += 1
                if choosen_digit == random_digit:
                    time.sleep(1)
                    print(f'Wow you guessed it. It\'s {random_digit} and number of attempts {attempt}.')
                    break
                elif attempt == n:
                    time.sleep(1)
                    print(f'Not today. It\' {random_digit}.')
                    time.sleep(1)
                elif choosen_digit > random_digit:
                    time.sleep(1)
                    print('Less')
                elif choosen_digit < random_digit:
                    time.sleep(1)
                    print('More')


def play_or_dead():
    print('Thanks for playing:)')
    time.sleep(1)
    play_again = input('If you want to restart the game. Press enter...\n')
    if play_again != '':
        return True


while True:
    load_game()
    number = number_of_attempts()
    start_game(number)
    if play_or_dead():
        break

# Task 2
# The birthday greeting program.

name, age = input('Write your name: ').title(), int(input('How old are you?: '))
print(f'Hello {name}, on your next birthday you’ll be {age + 1} years.')

# Task 3
# Words combination
from random import shuffle


def words_combination():
    string = [i for i in input('Write word: ')]
    for i in range(5):
        shuffle(string)
        print(''.join(string))


words_combination()

# Task 4
# The math quiz program
from random import randint


def math_adding():
    a, b = randint(1, 100), randint(1, 100)
    answer = int(input(f'Write your answer. {a} + {b} = '))
    if answer == a + b:
        print('You are right!')
    else:
        print('You have to go to school:(')


math_adding()
