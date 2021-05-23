with open('data_2.txt', 'r') as f:
    line_count = 0
    word_count = 0
    for line in f:
        for word in line.split():
            word_count += 1
        line_count += 1
    print(f'В файле data_2.txt {line_count} строк и {word_count} слов')
