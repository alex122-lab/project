# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

# Вариант решения № 1:
my_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите новый элемент рейтинга: '))
my_list.append(new_element)
my_list.sort(reverse=True)
print('Вариант решения № 1:', my_list)

# Вариант решения № 2:

my_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите новый элемент рейтинга: '))
count = 0
for num in my_list:
    if new_element > my_list[count]:
        my_list.insert(count, new_element)
        break
    elif count < len(my_list) - 1 and new_element == num and new_element > my_list[count + 1]:
        my_list.insert(count + 1, new_element)
        break
    elif count == len(my_list) - 1 and new_element <= num:
        my_list.append(new_element)
        break
    count += 1

print('Вариант решения № 2:', my_list)
