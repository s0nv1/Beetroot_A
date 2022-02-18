s = [1, 2, 3, 4, 5]
st = tuple(s)
print(st)
print(s.__sizeof__())
print(st.__sizeof__())
print(st.index(5))
print(st.count(3))


s = {1, 3, 4, 6, 3}
print(id(s))
text = tuple(s)
print(text)

textlist = [item for item in text]
print(textlist)

A = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")



a = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
print(id(a))
b = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
c = a + tuple(b)
print(a)
print(id(c))