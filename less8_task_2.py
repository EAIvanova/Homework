class MyException(Exception):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def calc(num_1, num_2):
        try:
            return f'Результат деления: {(num_1 / num_2):.2f}'
        except ZeroDivisionError:
            return f'Делить на 0 нельзя!'


user_input_1 = int(input("Введите делимое: "))
user_input_2 = int(input("Введите делитель: "))
a = MyException(user_input_1, user_input_2)
print(MyException.calc(user_input_1, user_input_2))
print(a.calc(2021, 12))
