open('data_5.txt', 'a+')
with open('data_5.txt', 'r+') as f:
    count = 0
    sum_num = 0
    for count in range(10):
        f.write(str(count) + ' ')
        sum_num += count
    print(f'Сумма чисел в файле = {sum_num}')


