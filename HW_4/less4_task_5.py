from functools import reduce


my_list = [i for i in range(100, 1001, 2)]
print(my_list)
result = reduce(lambda prev, cur: prev * cur, my_list)
print(result)
