# Task 1
# Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys
# and the number of occurrences as values.

dict_sentenc = dict([(item, ind) for ind, item in enumerate(input().split())])
print(dict_sentenc)

