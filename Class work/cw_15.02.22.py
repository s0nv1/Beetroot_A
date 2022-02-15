#1. Write a Python program that accepts a string and calculate the number of digits,
# letters in the input string
s = input()
digits = 0
letters = 0
for i in s:
    if i.isdigit():
        digits += 1
    elif i.isalnum():
        letters += 1
else:
    print(f'Digits: {digits}\nLetters: {letters}')

#2. Generate 5 random integers between 10 and 1000 which is divisible by 7
import random

count = 0
while count != 5:
    num = random.randint(10, 1000)
    if num % 7 == 0:
        print(num)
        count += 1

#3. Create a program that reads from the user input int and prints back the square root of this number
from math import sqrt

num = int(input())
print(sqrt(num))

#4.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.

for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=' ')
#5. Write a program that takes an integer from user input,
# stores it in variable n and prints an n-by-n table such that
# there is an `*` in row `i` and column `j` if the greatest common divisor of `i` and `j`
# is 1 (i and j are relatively prime) and a space character in that position otherwise
from math import gcd

num = int(input())
for i in range(1, num + 1):
    print()
    for j in range(1, num + 1):
        if gcd(i,j) == 1:
            print('*', end='')
        else:
            print(' ', end='')

#6. Write a Python program to convert temperatures to and from celsius, Fahrenheit.
# Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in Fahrenheit

tempC_or_F = int(input('Celsius = 1, Fahrenheit = 2.\nWhat temperature do you want to change to?: '))
if tempC_or_F == 1:
    faren = int(input('Input Fahrenheit temperature: '))
    print(f'Celsius temperature: {(5/9)*(faren-32)}')
else:
    cels = int(input('Input Celsius temperature: '))
    print(f'Fahrenheit temperature: {((cels - 32)/1.8)}')