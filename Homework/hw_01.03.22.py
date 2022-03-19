# Task 1
# A Person class

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old')


ex_person = Person('Carl', 'Johnson', 26)

ex_person.talk()

# Task 2
# Doggy age


class Dog:
    age_factor = 7

    def __init__(self, age_dog):
        self.age_dog = age_dog

    def human_age(self):
        return Dog.age_factor * self.age_dog


dog_s = Dog(5)

print(dog_s.human_age())

# Task 3
# TV controller

channels = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, CHANNELS):
        self.channels = CHANNELS


controller = TVController(channels)

print(controller.__dict__)
print(controller.channels[0])