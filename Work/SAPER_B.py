import random

t = [['X' for i in range(10)] for j in range(10)]

for i in t:
    print(*i, sep='   ')

s = [[j for j in range(1, 11)]for i in range(10)]

for i in range(len(s)):
    for j in range(random.randint(1, 3)):
        s[i][random.randint(0, 9)] = -1
s = [[j for j in range(random.randint(0, 9))]for i in range(len(s))]


for i in s:
    for j in i:
        print(j if j == -1 else ' ' + str(j), end='  ')
    print()
