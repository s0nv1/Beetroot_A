# Множества set()
s = set('world')
t = set('hello')
print(s)
print(len(s))
print('o' in s)
print(s.isdisjoint(t))
print(s == t)
print(s.issubset(t))
print(s.issuperset(t))
print(s.difference(t))

s.symmetric_difference_update(t)
print(s)
s.add('t')
print(s)
s.remove('t')
print(s)
s.discard('g')
print(s)
print(s.pop())
s.шт



