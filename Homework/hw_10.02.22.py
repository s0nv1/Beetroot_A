# Task 1 "The greeting program"
# 2 variables
name, day = 'team', 'thursday'
# Concatenate strings using + instruction.
# Used method .title() to print first character uppercase.
print("Good day " + name + "! " + day.title() + " is a perfect day to learn some python.")
# String formatting.
print(f'Good day {name}! {day.title()} is a perfect day to learn some python.')

print("Good day {}! {} is a perfect day to learn some python.".format(name, day.title()))

print("Good day %s! %s is a perfect day to learn some python." % (name, day.title()))
# Created 2 new variables included first and second part of full text.
first, second = f"Good day {name}! ", f"{day} is a perfect day to learn some python."
# Used method .capitalize() to print first character uppercase.
print(first + second.capitalize())

# Task 2 "Manipulate strings"
# 2 variables first and last name.
first_name, last_name = "Ihor", "Sapko"
# Used string concatenation to add them together with a white space in between.
full_name = first_name + ' ' + last_name
# Used string formatting.
print(f'Greetings {full_name}!')

# Task 3
# Using python as a calculator.
# I used arithmetic operators like '+, -, *, /, //, **, %'.
# Created a and b variables.
a, b = 5, 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)
