# Task 1
# String manipulation.
text = input()
if len(text) >= 2:
    print(text[:2] + text[-2:])
else:
    print('Empty String')

# Task 2
# The valid phone number program.
while True:
    phone_number = input('Write phone number: ')
    if phone_number.isdigit() and len(phone_number) == 10:
        print('Right phone number')
        break
    else:
        print('Not correct phone number, try again.')

# Task 3
# The name check.
my_name = 'ihor'
name = input('Write your name: ').lower()
if name == my_name: # print(name == my_name)
    print(True)
else:
    print(False)
