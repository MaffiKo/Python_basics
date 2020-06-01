import json
with open('text_77.json', 'a', encoding='utf-8') as text_json:

    with open('text_7.txt', 'r', encoding='utf-8') as text:
        company, company_prof, company_list = dict(), dict(), []
        all_profit_c, profit_c = 0, 0
        for i in text:
            name, form, value, cost = i.split()
            profit = int(value) - int(cost)
            if profit > 0:
                all_profit_c += profit
                profit_c += 1
            company_prof["average_profit"] = int(all_profit_c / profit_c)
            for n in name:
                company[name] = company.get(n, 0) + profit
        company_list = company, company_prof
        print(company_list)

    json.dump(company_list, text_json, ensure_ascii=False, indent=4)







# название, форма собственности, выручка, издержки.Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
