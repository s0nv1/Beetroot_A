# Task 1
# If I change the error to KeyError in the opps() function, the key_error() function will catch an error.
# And print the appropriate error text. If I leave an IndexError in opps(). I will get an IndexError.
def opps():
    raise IndexError


def key_error():
    try:
        opps()
    except IndexError:
        print('KeyError')


key_error()


# Task 2


def a_b():
    a, b = input(), input()
    try:
        return int(a) ** 2 / int(b)
    except ValueError:
        print('ValueError')
    except ZeroDivisionError:
        print('ZeroDivisionError')


print(a_b())

# Task 3
# TV controller

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    pass

    def __init__(self, channels):
        self.channels = channels
        self.channel_online = 0

    def first_channel(self):
        self.channel_online = 0
        return self.channels[self.channel_online]

    def last_channel(self):
        self.channel_online = 2
        return self.channels[self.channel_online]

    def turn_channel(self, n):
        self.channel_online = n - 1
        return self.channels[self.channel_online]

    def next_channel(self):
        self.channel_online = self.channel_online + 1 if self.channel_online < 2 else 0
        return self.channels[self.channel_online]

    def previous_channel(self):
        self.channel_online = self.channel_online - 1 if self.channel_online > 0 else 2
        return self.channels[self.channel_online]

    def current_channel(self):
        return self.channels[self.channel_online]

    def is_exist(self, *args):
        return 'YES' if type(args[0]) == int and 1 <= args[0] <= 3 else 'YES' if type(
            args[0]) == str and args[0] in self.channels else 'NO'


controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist('2'))
