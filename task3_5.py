def sum_num(result):
    summN = 0
    numbers = input('Введите строку чисел, разделенных пробелом, или N для остановки программы: ')
    for num in numbers.split():
        if num != 'N' and num != 'n':
            summN += int(num)
        else:
            result += summN
            print('Сумма чисел:', result)
            return
    result += summN
    print('Сумма чисел:', result)
    sum_num(result)

result = 0
summN =  sum_num(result)
