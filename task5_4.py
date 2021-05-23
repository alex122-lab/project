numbers = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
with open('data_4.txt', 'r') as f:
    for line in f:
        english_num = line.split(sep='-')[0]
        russian_num = numbers[english_num]
        list_line = list(line.split(sep='-'))
        list_line[0] = russian_num
        line = '-'.join(list_line)
        print(line)
        with open('data_4_out.txt', 'a') as f_out:
            f_out.write(line)
