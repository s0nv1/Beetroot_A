import random

count = 0
num = int(input())
low = 1
high = 100
while count != 7:
    mid = (int(low) + int(high)) // 2
    print(f'Моё число {mid}')
    count += 1
    if num == mid:
        print(f'Пк угадал число {mid}, количество попыток {count}.')
        break
    elif mid != num:
        print('Не правильно!')
        ask = input('Больше или меньше')
    if ask == 'б':
        low = mid + 1
    else:
        high = mid - 1
