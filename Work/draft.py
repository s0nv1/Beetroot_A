import random


presents = ['Winner', 'Losser', 'Losser']
random.shuffle(presents)
rand_door = {i + 1: presents[i] for i in range(3)}

x = int(input('Выбирите дверь 1, 2, 3: '))


if rand_door[x] == 'Winner':
    print(f'Я открываю пустую дверь. И это {}')







