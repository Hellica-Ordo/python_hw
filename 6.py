# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
from functools import reduce

lessons = {}

with open('lesson_5-6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        subject = line.split(':')[0]
        spliced_line = [''.join([v for v in w if v.isdigit()]) for w in line.split(':')[1].split('(')]
        number = reduce(lambda x, y: x+y, [int(f) for f in spliced_line if len(f) != 0])
        lessons[subject] = number
print(lessons)