from random import randint


class Matrix:

    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        s = ""
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                s += f'{self.nums[i][j]:02} '
            s += '\n'
        return s

    def __add__(self, other):
        num = [[self.nums[i][j] + other.nums[i][j]
                for j in range(len(self.nums[i]))] for i in range(len(self.nums))]
        return Matrix(num)


matrix_1 = Matrix([[randint(0, 21) for _ in range(5)] for _ in range(5)])
matrix_2 = Matrix([[randint(0, 21) for _ in range(5)] for _ in range(5)])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
