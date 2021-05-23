# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open('lesson_5-4.txt', 'r') as my_file:
    text = my_file.read()

with open('lesson_5-4-new.txt', 'w') as new_file:
    text = text.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре').replace('вЂ”', '—')
    new_file.writelines(text)