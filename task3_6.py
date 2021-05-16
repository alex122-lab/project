def int_func(word):
    listW = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v',
             'x', 'y', 'z', 'j', 'u', 'w'}
    if set(word).issubset(listW):
        word = word.title()
    print(word)

word = input('Введите слово: ')
int_func(word)

words = input('Введите строку слов через пробел: ')
for word in words.split():
    int_func(word)


