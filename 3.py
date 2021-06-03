# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.

class IsNotDigit(Exception):
    def __init__(self, text):
        self.text = text


class MyDigitsList:
    def __init__(self, digits_list):
        for i in digits_list.split():
            try:
                i = int(i)
                new_list.append(i)
            except Exception:
                print(IsNotDigit('Пожалуйста, вводите только числа.'))

new_list = []
list = []
while True:
    number = input('Введите число. Для завершения работы введите quit: ')
    if number != "quit":
        list = ''.join(number)
        check_check = MyDigitsList(list)
    else:
        print('Ваш список:', new_list)
        break