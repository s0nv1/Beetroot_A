
animals = set(['dog', 'cat', 'tiger', 'elephant', 'dog'])
sea_anomal = ['cow', 'dolphin', 'wolf']
animals.add('monkey')
print(animals)
animals.update(sea_anomal, {'bear'}, {'seacow'})
print(animals)
animals.discard('cat')
print(animals)
anipop = animals.pop()
print(anipop)
print(animals)

num = {1, 2, 3, 4,}
num2 = {3, 4, 5, 6}
s = num.union(num2)
number_same = num.intersection(num2)
number_inters = num.difference(num2)
sumetric_dif = num.symmetric_difference(num2)
print(sumetric_dif)
print(s)
print(number_inters)
print(number_same)