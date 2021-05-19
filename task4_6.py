from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el, end = ' ')

print()

с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el, end=' ')
    с += 1