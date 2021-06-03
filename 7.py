# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2
        self.comp_numb = 'num_1 + num_2 * i'

    def __add__(self, other):
        return f'Сумма комплексных чисел: {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        return f'Произведение комплексных чисел: {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_2 * other.num_1} * i'

    def __str__(self):
        return f'Ваши числа: {self.num_1} + {self.num_2} * i'


my_number1 = ComplexNumber(1, -2)
my_number2 = ComplexNumber(3, 4)
print(my_number1)
print(my_number1 + my_number2)
print(my_number1 * my_number2)