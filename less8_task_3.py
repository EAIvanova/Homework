class MyError:
    def __init__(self):
        self.my_list = []

    def user_input(self):
       while True:
            try:
                val = int(input('Введите значения и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list} \n ')
            except ValueError:
                print(f"Недопустимое значение - строка")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.user_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = MyError()
print(try_except.user_input())
