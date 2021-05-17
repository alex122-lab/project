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
