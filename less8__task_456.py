from datetime import datetime


class Store:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}
        self.my_store = []

    def take_to_store(self, equipment):
        # внесение в словарь название оборудования, серийный номер и время передачи на склад
        t = datetime.now()
        self.lists.update({equipment.serial_number: [equipment.title, self, t]})
        print(f'На склад {self.title} получено оборудование:{equipment.title}, '
              f'серийный номер - {str(equipment.serial_number)}, '
              f'Дата:{str(t.day)}.{str(t.month)}.{str(t.year)}')

    def give_to_store(self, equipment, other):
        # передача оборудование на другой склад
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title, other, t]})
        print(f'Передано оборудование:{equipment.title} '
              f'серийный номер - {str(equipment.serial_number)}, '
              f'Дата:{str(t.day)}.{str(t.month)}.{str(t.year)}')
        other.take_to_store(equipment)

    def list_equipments(self):
        print(f'На склад {self.title} получено оборудование: {self.lists}')
        print(f'Общее количество:{len(self.lists)}')
        print(f'Со склада {self.title} выдано оборудование: {self.give_lists}')
        print(f'Общее количество: {len(self.give_lists)}')

    def valid_reception(self):
        while True:
            try:
                quantity = int(input(f'Введите количество принтеров, отправленных на склад: '))
                self.my_store.append(quantity)
                print(f'Количество принтеров, отправленных на склад: {self.my_store}')
            except ValueError:
                print(f'Ошибка ввода данных')
            break


class OfficeEquipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)


class Printer(OfficeEquipment):
    def __init__(self, title, serial_number, print_velocity):
        OfficeEquipment.__init__(self, title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return f'Название модели: {OfficeEquipment.__str__(self)}. ' \
               f'Параметры: {str(self.print_velocity)}'


class Scanner(OfficeEquipment):
    def __init__(self, title, serial_number, resolution):
        OfficeEquipment.__init__(self, title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return f'Название модели: {OfficeEquipment.__str__(self)}. ' \
               f'Параметры: {str(self.resolution)}'


class Copier(OfficeEquipment):
    def __init__(self, title, serial_number, copy_quality):
        OfficeEquipment.__init__(self, title, serial_number)
        self.copy_quality = copy_quality

    def __str__(self):
        return f'Название модели: {OfficeEquipment.__str__(self)}. ' \
               f'Параметры: {str(self.copy_quality)}'


store1 = Store('Head Store')
store2 = Store('Secondary Store')
a = Printer('HP', 350035, 50)
b = Scanner('Samsung', 670067, 400)
c = Copier('LG', 750075, 1000)
d = Scanner('Samsung', 670068, 200)

print(a)
print(b)
print(c)
print(d)

store1.take_to_store(a)
store1.take_to_store(b)
store1.take_to_store(c)
store1.take_to_store(d)

store1.give_to_store(a, store2)
store1.list_equipments()
store2.list_equipments()

store2.valid_reception()
