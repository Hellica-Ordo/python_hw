# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

sample_list = []

while True:
    item = (input('Добавьте элемент списка или введите "список закончен": '))
    sample_list.append(item)
    if item == 'список закончен':
        break

sample_list.remove('список закончен')
print('Список сформирован.')

count = 0
for i in range(int(len(sample_list) / 2)):
    sample_list[count], sample_list[count + 1] = sample_list[count + 1], sample_list[count]
    count += 2

print(sample_list)