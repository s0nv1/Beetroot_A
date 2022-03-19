import random, time

presents = ['winner', 'losser', 'losser']


def choose_door():
    print('Хочешь стать обладателем машини, выбери одну дверь!')
    time.sleep(1)
    return int(input('Выбирай одну дверь 1, 2, 3: '))


def open_empty_door(door):
    if door == 1:
        if doors_presents[2] == 'losser':
            return 2
        elif doors_presents[3] == 'losser':
            return 3
    elif door == 2:
        if doors_presents[1] == 'losser':
            return 1
        elif doors_presents[3] == 'losser':
            return 3
    else:
        if doors_presents[2] == 'losser':
            return 2
        elif doors_presents[1] == 'losser':
            return 1


def change_door(empty):
    print(f'Открывыю пустую дверь и это: {empty}')
    time.sleep(1)
    print(f'Ты выбрал {user_door}, но можешь поменять свой выбор на {6 - user_door - empty_door}')
    return int(input(f'{user_door} или {6 - user_door - empty_door}'))


def win_or_loss(number_door):
    if doors_presents[number_door] == 'winner':
        print('\nУ нас есть победитель! Ты выиграл Tesla model X!')
    else:
        print('\nДверь открывыеться... Сегодня не твой день*(')


while True:
    random.shuffle(presents)
    doors_presents = {i + 1: presents[i] for i in range(3)}
    user_door = choose_door()
    empty_door = open_empty_door(user_door)
    result = change_door(empty_door)
    win_or_loss(result)
    ask = input('Попробуешь ещё раз (да или нет): ')
    if ask in 'да':
        continue
    else:
        break