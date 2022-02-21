import copy
import random
list1 = [random.randint(1,100) for i in range(50)]
count = len(list1) - 1
list2 = []
while count != -1:
    list2.append(list1[count])
    count -= 1
print(list1)
print(list2)

import copy
count = 0
list3 = []
while count != len(list1):
    list3.append(copy.copy(list1[count]))
    count += 1
else:
    print(list3)
    print(id(list1))
    print(id(list3))

    # adress = {input(): int(input()) for i in range(5)}
    # print(adress)
    # name = ['Dany', 'Misha', 'Grisha', 'Ilona']
    # num_tel = [[3809945, 7], [366545, 4], [3804443242, 5], [380213124, 9]]
    # adress2 = {key: num_tel[name.index(key)] for key in name}
    # print(adress2)
