t = (1,)
print(type(t))

tup1 = ('physics', ['chemistry'], {1: 'hello', 2: 'bay bay'}, 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
tup1[1].append('slhool')
tup1[1].extend(['me', 'boy'])
tup1[1].insert(2, 'love')
tup1[1].reverse()
tup1[1].sort()
tup1[1].pop(1)
tup1[1].remove('slhool')
print(tup1[1].index('love'))
print(tup1[1].count('me'))
tup1[1].clear()
tup1[1].extend([1, 2, 3, 4, 5])
print(len(tup1[1]))
print(max(tup1[1]))
print(min(tup1[1]))
print(sum(tup1[1]))
s = tup1

print(id(tup1))
print(id(s))

s[1].append(6)
print(s)
print(tup1)

import copy

t = copy.deepcopy(s)
r = copy.copy(s)
print(id(t))
print(id(s))
r[2][2] = 'poka poka'
print(t)
print(s)
print(tup1)
print(r)
print(t.index(1997))
print(t.count(2000))

print(id(t[1]))
print(len(t[1]))
qwe = t
print(qwe)
print(3 in qwe[1])
print(1 in qwe[2])
for ind in qwe[2].values():
    print(f'index:{ind}')