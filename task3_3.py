def my_func_min(x, y):
    if x <= y:
        min = x
    else:
        min = y
    return min

def my_func(num_1, num_2, num_3):
    summ_num = num_1 + num_2 + num_3 - my_func_min(my_func_min(num_1, num_2), my_func_min(num_1, num_3))
    return summ_num


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

print('\nСумма двух наибольших аргументов равна:', my_func(num_1, num_2, num_3))