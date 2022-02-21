class Cell:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return Cell(self.param + other.param)

    def __sub__(self, other):
        result = self.param - other.param
        if result > 0:
            return Cell(result)
        else:
            print("Ошибка вычитания!")

    def __mul__(self, other):
        return Cell(self.param * other.param)

    def __truediv__(self, other):
        return Cell(self.param // other.param)

    def make_order(self, numb):
        s = ''
        for i in range(self.param // numb):
            s += '*' * numb + '\n'
        s += '*' * (self.param % numb) + '\n'
        return s

    def __str__(self):
        return f'{self.param}'


cell_1 = Cell(35)
print(cell_1.make_order(4))
cell_2 = Cell(12)
print(cell_2.make_order(5))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2 - cell_1)
