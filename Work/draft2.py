s = [5, 1, 4, 3, 2]

print(len(s))
print(max(s))
print(min(s))
s.sort()
print(s)
s.reverse()
print(s)

print( 2 in s)
print(6 in s)
print(6 not in s)
t = 'hello'
s.append(t)
s.extend(t)
print(s)
text = s.copy()
tet = s[:]
print(text)
print(id(text))
print(id(tet))
print(id(s))
print(s)
print(s.count('l'))
print(s.pop(4))
print(s)
s.insert(4, 1)
print(s)
ser = [5, 7, 10]
s.extend(ser)
print(s)
print(s.index(5, 5))
del s[5:12]
print(s)
s.sort(reverse=True)
print(s)
print(id(s))
s.remove(10)
print(s)
s.insert(0, 10)
print(s)

print(s[:4])
print(s[4:])
print(s[:])
print(s[::-1])
print(s[0])

ser += s
print(ser)
print(list(set(ser)))