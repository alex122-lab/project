class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    try:
        value = input('Введите целое число в список или stop для выхода из программы: ')
        if not value.isdigit() and not value[1:].isdigit():
            raise OwnError("Вы не ввели целое число!")
    except OwnError as err:
        if value == 'stop':
            break
        print(err)
    else:
        my_list.append(int(value))
print('Ваш список:', my_list)

