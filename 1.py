# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_string):
        self.date_string = str(date_string)

    @classmethod
    def string_to_numbers(cls, date_string):
        date_numbers = date_string.split('-')
        return int(date_numbers[0]), int(date_numbers[1]), int(date_numbers[2])

    @staticmethod
    def date_validation(date_string):
        day = int(date_string.split('-')[0])
        month = int(date_string.split('-')[1])
        if 1 <= day <= 31 and 1 <= month <= 12:
            return 'Корректная дата.'
        else:
            if day > 31 or day < 1:
                return 'Неправильный день!'
            elif month > 12 or month < 1:
                return 'Неправильный месяц!'


print(Date.string_to_numbers('02-06-2021'))
print(Date.date_validation('33-13-2020'))