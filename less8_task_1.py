class MyData:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def get_data(cls, dd_mm_yyyy):
        my_date = []
        for i in dd_mm_yyyy.split():
            if i != '-':
                my_date.append(i)
        return f'{int(my_date[0])}, {int(my_date[1])}, {int(my_date[2])}'

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year > 0:
                    return f'Верно: {day}-{month}-{year}'
                else:
                    return f"Неверный год: {year}"
            else:
                return f"Неверный месяц: {month}"
        else:
            return f"Неверный день: {day}"


my_day = MyData('21 - 07 - 2010')
print(my_day.valid(14, 9, 0000))
print(my_day.valid(5, 20, 1978))
print(my_day.valid(75, 2, 1999))

print(my_day.get_data('09 - 12 - 2001'))
print(my_day.get_data('25 - 05 - 2020'))
print(my_day.valid(31, 12, 2021))
