num_from_1_to_100 = [i for i in range(1, 101)]
new_list = []
for i in range(0, len(num_from_1_to_100), 7):
    if num_from_1_to_100[i] % 5 != 0:
        new_list.append(num_from_1_to_100[i] - 1)
del new_list[0]
print(*new_list)

