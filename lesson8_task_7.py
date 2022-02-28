class ComplexNumb:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        result_1 = self.param[0] + other.param[0]
        result_2 = self.param[1] + other.param[1]
        if result_2 > 0:
            return f" ({result_1} + {result_2}i)"
        elif result_2 == 0:
            return f" {result_1}"
        else:
            return f" ({result_1} {result_2}i)"

    def __mul__(self, other):
        res_1 = self.param[0] * other.param[0]
        res_2 = self.param[0] * other.param[1] + self.param[1] * other.param[0]
        res_3 = self.param[1] * other.param[1]
        if res_2 > 0:
            return f" ({res_1 - res_3} + {res_2}i)"
        elif res_2 == 0:
            return f" {res_1 - res_3}"
        else:
            return f" ({res_1 - res_3} {res_2}i)"

    def __str__(self):
        return f'{self.param}'


com_num_1 = [2, 3]
com_num_2 = [4, 5]
c_1 = ComplexNumb(com_num_1)
c_2 = ComplexNumb(com_num_2)
print(c_1 + c_2)
print(c_1 * c_2)
cn_1 = [3, -8]
cn_2 = [6, 3]
c_3 = ComplexNumb(cn_1)
c_4 = ComplexNumb(cn_2)
print(c_3 + c_4)
print(c_3 * c_4)
