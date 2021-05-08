words = input('Введите несколько слов через пробел: ')
count = 1
for word in words.split():
    print(f'{count} {word[:10]}')
    count += 1
