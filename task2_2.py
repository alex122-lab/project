count = int(input('Введите количество элементов списка: '))
list_1 = []
for i in range(count):
    new_element = input(f'Введите {i}-й элемент списка: ')
    list_1.append(new_element)
print(f'начальный список {list_1}')

for i in range(0, count, 2):
    if count % 2 == 0 or (count % 2 != 0 and i != count - 1):
        list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
print(f'конечный список {list_1}')
