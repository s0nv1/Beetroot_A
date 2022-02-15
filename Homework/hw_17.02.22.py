# Task 1
# The greatest number
import random

list_num = [random.randint(1, 100) for i in range(10)]
count = 0
max_digit = 0
while count != len(list_num):
    if list_num[count] > max_digit:
        max_digit = list_num[count]
    count += 1
else:
    print(max_digit)

# for loop
for i in list_num:
    if i > max_digit:
        max_digit = i
print(max_digit)
# max()
print(max(list_num))
# Task 2
# Exclusive common numbers.
import random

rand_list, rand_list_second = list(set([random.randint(1, 10) for i in range(10)])),\
                              list(set([random.randint(1, 10) for j in range(10)]))
same_digits = []
count = 0
while count != len(rand_list):
    if rand_list[count] in rand_list_second:
        same_digits.append(rand_list[count])
    count += 1
else:
    print(*same_digits)

# Task 3
# Extracting numbers.
count = 0
num_from_1_to_100 = []
new_list = []
while count != 100:
    count += 1
    num_from_1_to_100.append(count)
else:
    while count != 0:
        count -= 1
        if num_from_1_to_100[count] % 7 == 0 and num_from_1_to_100[count] % 5 != 0:
            new_list.append(num_from_1_to_100[count])
    new_list.sort()
    print(*new_list)

# Second variant with for loop.
num_from_1_to_100 = [i for i in range(1, 101)]
new_list = []
for i in num_from_1_to_100:
    if i % 7 == 0 and i % 5 != 0:
        new_list.append(i)
print(*new_list)
