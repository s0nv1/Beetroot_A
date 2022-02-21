# dict_sentence = {item: ind for item input().split()}
# print(dict_sentence)

# n = input().split()
# d = {}
# for i in n:
#     count = 1
#     for j in n[n.index(i) + 1:]:
#         if i == j:
#             count += 1
#     d[i] = count
# print(d)
sentence = input().split()
dict_sentence = {i: sentence.count(i) for i in sentence}
print(dict_sentence)