# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени
# года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

monthNumber = int(input('Введите номер месяца: '))
list_M = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

winter = list_M[0:3]
spring = list_M[3:6]
summer = list_M[6:9]
fall = list_M[9:12]

while monthNumber not in list_M:
    monthNumber = int(input('Некорректный ввод, попробуйте еще раз - введите номер месяца: '))

# Решение № 1

if monthNumber in winter:
    season = 'зима'
elif monthNumber in spring:
    season = 'весна'
elif monthNumber in summer:
    season = 'лето'
else:
    season = 'осень'
print('Решение № 1: Месяц относится к времени года -', season)

# Решение № 2

monthes = dict(winter=winter, spring=spring, summer=summer, fall=fall)

if monthNumber in monthes.get('winter'):
    season = 'зима'
elif monthNumber in monthes.get('spring'):
    season = 'весна'
elif monthNumber in monthes.get('summer'):
    season = 'лето'
else:
    season = 'осень'
print('Решение № 2: Месяц относится к времени года -', season)