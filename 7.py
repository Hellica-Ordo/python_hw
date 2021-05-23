# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.


with open ('lesson_5-7.txt', 'r', encoding = 'utf-8') as my_file:
    text_file = my_file.readlines()
    firms_count = 0
    for i in text_file:
        firms_count += 1
    print('Количество фирм в списке:', firms_count)

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('lesson_5-7.txt', 'r', encoding = 'utf-8') as my_file:
    for line in my_file:
        name, firm, income, losses = line.split()
        profit[name] = int(income) - int(losses)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    prof_aver = prof / i
    print(f'Средняя прибыль: {prof_aver:.2f}')
    print(f'Прибыль каждой компании: {profit}')

with open('lesson_5-7.json', 'w', encoding = 'utf-8') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print('Создан файл с расширением json')