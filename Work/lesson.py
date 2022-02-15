from math import gcd


num = int(input())
for i in range(1, num + 1):
    print()
    for j in range(1, num + 1):
        if gcd(i,j) == 1:
            print('*', end='')
        else:
            print(' ', end='')



#s = input('C or F: ')
#num = int(input())
#if s == "F":
#    print(int((5/9)*(num-32)))
#else:
#    print(int((num - 32)/1.8))

while True:
    try:
        c, m, y, k = float(input()), float(input()), float(input()), float(input())
    except ValueError:
        print('ValueError')

white = 1 - k

print(f'Red : {255 * white * (1 - c)}')
print(f'Green : {255 * white * (1 - m)}')
print(f'Blue : {255 * white * (1 - y)}')