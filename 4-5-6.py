# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# class OfficeMachines:
#     def __init__(self, name, color, cost):
#         self.name = name
#         self.color = color
#         self.cost = cost
# class Warehouse:
#     def __init__(self):
#         self.printer = Printer('HP', 'white', 3250)
#         self.scanner = Scaner('Canon', 'white', 2700)
#         self.copier = Copier('Xerox', 'white', 4750)
#
#     def receive_machine(self):
#         while True:
#             new_items = input('Введите название товара, количество, цену и год покупки. Для завершения программы введите quit: ')
#             if new_items != "quit":
#                 list = []
#                 list.append(new_items.split())
#                 try:
#                     list[0][1] = int(list[0][1])
#                     list[0][2] = int(list[0][2])
#                     avito.received(list)
#                 except:
#                     print('Ошибка ввода данных.')
#
#             else:
#                 break
#
#         def received(self, received_dict):
#             received_dict = {'Название': received_dict[0][4], 'Количествово': income_dict[0][1], 'Цена': income_dict[0][2], 'Год покупки': income_dict[0][3]}
#         # try:
#         #     unit = input('Введите наименование: ')
#         #     cost = int(input('Введите стоимость: '))
#         #     unique = {'Модель устройства': unit, 'Количество': cost}
#         #     self.my_unit.update(unique)
#         #     self.my_store.append(self.my_unit)
#         #     print(f'Текущий список -\n {self.my_store}')
#         # except Exception:
#         #     print(StoreError('Пожалуйста, вводите только числа.'))
#         #
#         # print('Для выхода введите quit')
#         # q = input(f'---> ')
#         # if q == 'Q' or q == 'q':
#         #     self.my_store_full.append(self.my_store)
#         #     print(f'Весь склад -\n {self.my_store_full}')
#         #     return f'Выход'
#         # else:
#         #     return Warehouse.receive_machine(self)
#
# # unit_1 = Printer('HP', '25-05-20', 2)
# # unit_2 = Scaner('Canon', 'white', 2700)
# # unit_3 = Copier('Xerox', 'white', 4750)
# # print(unit_1.receipt_machine())
# # print(unit_2.receipt_machine())
# # print(unit_3.receipt_machine())
# # print(unit_1.printing())
# # print(unit_3.copying())
#
# avito = Warehouse()
# avito.receive_machine()


class OfficeMachines:

    def __init__(self, name, year, quantity, number_of_lists, *args):
        self.name = name
        self.year = year
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Название': self.name, 'Год покупки': self.year, 'Количество': self.quantity}

    # def __str__(self):
    #     return f'{self.name} цена {self.price} количество {self.quantity}'

    def receive(self):
        try:
            unit = input('Введите название: ')
            unit_cost = int(input('Введите цену: '))
            unit_quantity = int(input('Введите количество: '))
            unique = {'Модель': unit, 'Цена': unit_cost, 'Количество': unit_quantity}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
        except:
            return 'Неверные данные.'

        while True:
            next_item = input('Для выхода введите quit, для продолжения введите yes.')
            if next_item == 'yes':
                return OfficeMachines.receive(self)
            elif next_item == 'quit':
                self.my_store_full.append(self.my_store)
                print(f'На складе: {self.my_store_full}')
                break




class Printer(OfficeMachines):
    color_scale = 'цветной'
    def printing(self):
        return 'Принтер начинает печатать.'

class Scaner(OfficeMachines):
    dpi = 300
    def scanning(self):
        return 'Сканер начинает сканировать.'

class Copier(OfficeMachines):
    speed = 10
    def copying(self):
        return 'Копир начинает копировать.'


my_printer = Printer('HP', 2000, 5, 10)
my_scaner = Scaner('Canon', 1200, 5, 10)
my_copier = Copier('Xerox', 1500, 1, 15)
print(my_printer.receive())
print(my_scaner.receive())
print(my_copier.receive())
print(my_scaner.scanning())