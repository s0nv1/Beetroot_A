import random

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z']

adress = {}
for j in range(10):
    name = ''
    for i in range(4):
        name += random.choice(alph)
    num_tel = [random.randint(1000000000, 9999999999), random.randint(1, 10)]
    adress[name] = num_tel


while True:
    try:
        text = int(input(f'Список друзей: {[key for key in adress.keys()]}\nWrite (ask = 1 , del = 2, add = 3, average = 4, quit = 5): '))
    except ValueError:
        print('Try again, only digits!')
    else:
        if text == 1:
            name_friend = input('Write name: ')
            print(f'Telnum: {adress[name_friend][0]}, Friends:{adress[name_friend][1]}\n')
        elif text == 2:
            del_friend = input('Write name: ')
            print(f'Contact del {del_friend}\n')
            del adress[del_friend]
        elif text == 3:
            add_friend = input('New name: ')
            tell = int(input('Write telefone: '))
            friend_count = int(input('Count of friend: '))
            adress[add_friend] = [tell, friend_count]
            print(f'Add new contact: {add_friend}')
        elif text == 4:
            sum_f = 0
            for count in adress:
                sum_f += adress[count][1]
            average = sum_f / len(adress)
            print(f'Average of friends: {int(average)}\n')
        elif text == 5:
            break
        else:
            print('from 1 to 5!')
