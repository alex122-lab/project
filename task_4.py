# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input('Введите целое положительное число: '))
max = 0
while number > 0:
    numeral = number % 10
    number //= 10
    if numeral > max:
        max = numeral
print(max)

