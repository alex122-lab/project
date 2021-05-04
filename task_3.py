# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = int(input('Введите число: '))
summ_1 = number + int(str(number) * 2) + int(str(number) * 3)
print(summ_1)
