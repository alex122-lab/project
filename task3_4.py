def my_func(x, y):
    count = x ** y
    return count

def my_func_2(x, y):
    count = 1
    for i in range(abs(y)):
        count *= 1 / x
    return count
x = float(input('Введите действительное число: '))
y = int(input('Введите целое отрицательное число: '))

count = my_func(x, y)
print('\nРезультат возведения в степень:', count)

count = my_func_2(x, y)
print('\nРезультат возведения в степень:', count)