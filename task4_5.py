from functools import reduce

def mult_list(el_1, el_2):
    return el_1 * el_2
my_list = [el for el in range(100, 1001, 2)]

print(f'Список\n{my_list}\nРезультат вычисления произведения всех элементов списка:\n{reduce(mult_list, my_list)}')


