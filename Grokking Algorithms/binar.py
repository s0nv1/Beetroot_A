s = [i for i in range(1, 11)]

def bunary_search(list1, item):
    low = 0
    high = len(list1) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = list1[mid]
        if round(guess) == item:
            print(count)
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(bunary_search(s, 3))

count = 0
s = 4_000_000_000

while s !=0:
    count += 1
    s //= 2
print(count)