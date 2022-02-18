
countries = ['Ukraine', 'Belarus', 'France', 'Germany',
             'Estonia', 'Finland', 'Poland', 'Serbia']

for i, contry in enumerate(countries):
    countries[i] = contry, i + 1
print(countries)

sevens = []

for i in range(0, 71, 7):
    sevens.append(i)
print(sevens)

sevens = []
i = 0
while i <= 70:
    sevens.append(i)
    i += 7
print(sevens)

import random

points = 0
while True:
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    print(f'points: {points}')
    answer = input(f'{x} + {y} =? (type q to quit): ')
    if answer == 'q':
        break
    elif int(answer) != x+y:
        print('No points for you!')
        continue
    print('Goob job')
    points += 1

help(enumerate)