# Task 1
# Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys
# and the number of occurrences as values.

dict_sentence = dict([(item, ind) for ind, item in enumerate(input().split())])
print(dict_sentence)

# Task 2
# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.
# Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def total_price_of_stoke(a, b):
    return dict([(key, value * b[key]) for key, value in a.items()])


total_price = total_price_of_stoke(stock, prices)
print(total_price)

# Task 3
# List comprehension exercise

tuple_list = [(x, x ** 2) for x in range(1, 11)]
print(tuple_list)
