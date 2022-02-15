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

