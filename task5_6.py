schedule = {}
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
with open('data_6.txt', 'r') as f:
    for line in f:
        key = line.split()[0][:-1]
        value = line.split()[1] + line.split()[2] + line.split()[3]
        sum_num = 0
        number = ''
        for num in value:
            if num in numbers:
                number += num
            elif num == '(':
                sum_num += int(number)
                number = ''
        schedule[key] = sum_num
    print(schedule)
