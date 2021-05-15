# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    list = sorted([num_1, num_2, num_3])
    sum_1, sum_2 = list[1], list[2]
    return sum_1 + sum_2

print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))