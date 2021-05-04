# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.
timeSecond = int(input('Введите время в секундах: '))
hour = timeSecond // 3600
minute= timeSecond // 60 - hour * 60
second = timeSecond - minute * 60 - hour * 3600
print(f'{hour:02d}:{minute:02d}:{second:02d}')