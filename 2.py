# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class UnableDivision(Exception):
    def __init__(self, text):
        self.text = text


def division():
    try:
        divisible = int(input('Введите делимое число: '))
        dividing = int(input('Введите делитель: '))
        if dividing == 0:
            raise UnableDivision('Делить на ноль нельзя!')
        else:
            print(f'Результат деления: {divisible / dividing}')
    except ValueError:
        print('Пожалуйста, вводите только числа.')
    except UnableDivision as err:
        print(err)

print(division())