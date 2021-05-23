# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('lesson_5-5.txt', 'w') as my_file:
    print(input('Введите через пробел числа, которые вы хотите сложить: '), file = my_file)

with open('lesson_5-5.txt', 'r') as my_file:
    content = my_file.read()
    all_nums = 0
    for i in content.split(' '):
        if i.isdigit():
            all_nums = all_nums + int(i)

    print('Сумма чисел равна', all_nums)