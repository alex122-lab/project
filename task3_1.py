def divide(num_1, num_2):
    if num_2 != 0:
        result = num_1 / num_2
        print(' Результат деления:', result)
    else:
        print('Ошибка ввода - второе число не должно быть равно нулю')

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число, не равное нулю: '))

divide(num_1, num_2)
