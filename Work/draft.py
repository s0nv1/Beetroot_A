
while True:
    try:
        c, m, y, k = float(input()), float(input()), float(input()), float(input())
    except ValueError:
        print('ValueError')

white = 1 - k

print(f'Red : {255 * white * (1 - c)}')
print(f'Green : {255 * white * (1 - m)}')
print(f'Blue : {255 * white * (1 - y)}')