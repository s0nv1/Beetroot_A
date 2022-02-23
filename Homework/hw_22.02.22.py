# Task 1
# A simple function.
fav_movie = input()


def favorite_movie(movie):
    print(f'My favorite movie is named {movie}')


favorite_movie(fav_movie)
# Task 2
# Creating a dictionary.
country, capital = input('Input country: '), input('Input capital: ')


def make_country(contry, capitel):
    return {contry: capitel}


print(make_country(country, capital))

# Task 3
# A simple calculator.


def make_operation(*args):
    if args[0] == '+':
        print(sum(args[1:]))
    elif args[0] == '-':
        total = args[1]
        for i in args[2:]:
            total -= i
        print(total)
    else:
        total = args[1]
        for i in args[2:]:
            total *= i
        print(total)


make_operation('+', 5, 5, -10, -20)
