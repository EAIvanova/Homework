class MyException(Exception):
    pass

    @staticmethod
    def calc(num_1, num_2):
        if num_2 == 0:
            raise ZeroDivisionError('Делить на 0 нельзя!')
        return f'Результат деления: {(num_1 / num_2):.2f}'


user_input_1 = int(input("Введите делимое: "))
user_input_2 = int(input("Введите делитель: "))
a = MyException(user_input_1, user_input_2)
print(MyException.calc(user_input_1, user_input_2))
print(a.calc(2021, 12))
