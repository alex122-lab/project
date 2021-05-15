def int_func(word):
    word = word.title()
    print(word)

word = input('Введите слово: ')
int_func(word)

words = input('Введите строку слов через пробел: ')
for word in words.split():
    int_func(word)


