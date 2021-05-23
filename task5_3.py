def calculation():
    with open('data_3.txt', 'r') as f:
        num_income = 0
        num_employees = 0
        print(f'Сотрудники, имеющие оклад менее 20 тыс. руб.:')
        for line in f:
            sername = line.split()[0]
            income = line.split()[1]
            num_income += int(income)
            num_employees += 1
            if int(income) < 20:
                print(sername)
        return num_income / num_employees

print(f'\nСредняя зарплата сотрудников: {calculation()}')
