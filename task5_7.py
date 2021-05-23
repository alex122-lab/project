import json
list_firm = []
dict_firm = {}

with open('data_7.txt', 'r') as f:
    count_line = len([0 for _ in f])
    f.seek(0)
    count = 0
    count_average = 0
    total_profit = 0
    average_profit = 0
    for line in f:
        if count <= count_line:
            key = line.split()[0]
            profit = int(line.split()[2]) - int(line.split()[3])
            dict_firm[key] = profit
            count += 1
            if profit > 0:
                total_profit += profit
                count_average += 1
                average_profit = total_profit / count_average

    list_firm = [dict_firm, {'average_profit': average_profit}]
    print(list_firm)
    with open("data_7.json", "w") as write_f:
        json.dump(list_firm, write_f)



