werehouse = []
scroll = int(input('Введите количество товаров: '))
for i in range(scroll):
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    count = int(input('Введите количество товара: '))
    product = [i + 1, {
        'название': name,
        'цена': price,
        'количество': count,
        'eд': 'шт.'
    }]
    werehouse.append(tuple(product))
print('Готовая структура: ', werehouse)

products = {}
for i in range(len(werehouse)):
    products.setdefault('название', []).append(werehouse[i][1]['название'])
    products.setdefault('цена', []).append(werehouse[i][1]['цена'])
    products.setdefault('количество', []).append(werehouse[i][1]['количество'])
    products['eд'] = ['шт.']

print('Аналитика о товарах, собранная в словаре: ', products)




