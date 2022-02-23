#
# def func(x):
#     def add(a):
#         return x + a
#     return add
# test = func(100)
#
# print(test(200))

# def pas(r, w, y=2):
#     res = r + w
#     res *= y
#     return res
# print(pas(2, 7))

# def func(**kwargs):
#     return kwargs
#
# print(func(short='long', longer='longer'))
#
# add = lambda x, y: x * y
# print(add('q', 2))
# print((lambda x, y: x * y)(6, 6))
#
# fun = lambda *args: args
# print(type(fun(1, 2, 2.2, 33)))

# import random, copy
#
# tup = tuple(random.randint(1, 10) for i in range(10))
# print(tup)
# print(sum(tup)/len(tup))
# s = copy.copy(tup)
# print(id(tup))
# print(id(s))
#
# text = [(random.randint(1, 1)) for i in range(10) ]
# print(text)
# if len(set(text)) == 1:
#     print(True)
# else:
#     print(False)


# a = set([1, 2, 3, 4])
# b = set([3, 4, 7, 8])
# print(a.union(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.intersection(b))

# print([i for i in range(1, 11) if i % 2 == 0], [i for i in range(1, 11) if i % 2 == 1])
#
# print([(i, i) for i in range(10)])


