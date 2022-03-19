import random

s = [[j for j in range(1, 11)]for i in range(10)]
x_main = [['X' for i in range(10)] for j in range(10)]



for i in range(len(s)):
    for j in range(random.randint(1, 3)):
        s[i][random.randint(0, 9)] = -1

for i in s:
    for j in i:
        if j != -1:
            s[s.index(i)][i.index(j)] = 0


for i in range(10):
    for j in range(10):
        count = 0
        if s[i][j] == 0:
            try:
                for cow in range(-1, 2):
                    try:
                        for row in range(-1, 2):
                            if s[i + cow][j + row] == -1 and 0 <= i + cow <= 9 and 0 <= j + row <= 9:
                                count += 1
                    except:
                        s[i][j] = 0
                    else:
                        s[i][j] = count
            except:
                s[i][j] = 0
            else:
                s[i][j] = count

x_main = [['X' for i in range(10)] for j in range(10)]
for i in x_main:
    for j in i:
        print(j if j == -1 else ' ' + str(j), end='  ')
    print()


while True:
    user_x = int(input('Введите координаты клетки по Х: ')) - 1
    user_y = int(input('Введите координаты клетки по Y: ')) - 1
    if s[user_x][user_y] != -1:
        x_main[user_x][user_y] = s[user_x][user_y]
        for i in x_main:
            for j in i:
                print(j if j == -1 else ' ' + str(j), end='  ')
            print()
    else:
        print('You losser!')
        x_main[user_x][user_y] = s[user_x][user_y]
        for i in x_main:
            for j in i:
                print(j if j == -1 else ' ' + str(j), end='  ')
            print()
        break