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

