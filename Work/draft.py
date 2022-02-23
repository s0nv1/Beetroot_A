
def opps():
    raise IndexError


def key_error():
    try:
        opps()
    except KeyError:
        print('KeyError')

key_error()