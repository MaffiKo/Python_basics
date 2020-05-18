numbers = int(input("Сколько товаров вы хотите ввести? "))

n = 1
dict_goods = []
list_goods = []
analys_goods = []

while numbers >= n:
    name = str(input(f"Введите название товара №{n}- "))
    cost = int(input("Укажите его цену - "))
    quantity = int(input("Запишите количество - "))
    how_called = str(input("Укажите еденицу измерения - "))
    dict_goods = dict({'название': name, 'цена': cost, 'количество': quantity, 'eд': how_called})
    list_goods.append((n, dict_goods))
    n += 1

    analys_goods = dict(
        {'название': dict_goods.get('название'), 'цена': dict_goods.get('цена'),
         'количество': dict_goods.get('количество'), 'eд': dict_goods.get('eд')})
#  !С аналитикой возникла проблема, не смогла найти способ вывода аналитики всех товаров, получается только последнего

print(f'Список товаров: {list_goods}')
print(f'Аналитика товаров: {analys_goods}')
