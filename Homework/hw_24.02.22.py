# Task 1
# If I change the error to KeyError in the opps() function, the key_error() function will catch an error.
# And print the appropriate error text. If we leave an IndexError in opps(). I will get an IndexError.
def opps():
    raise IndexError


def key_error():
    try:
        opps()
    except KeyError:
        print('KeyError')


key_error()
# Task 2


def a_b():
    a, b = input(), input()
    try:
        return int(a)**2 / int(b)
    except ValueError:
        print('ValueError')
    except ZeroDivisionError:
        print('ZeroDivisionError')


print(a_b())
