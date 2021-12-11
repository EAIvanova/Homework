from functools import reduce
my_list = []

for i in range(100, 1001, 2):
    my_list.append(i)
print(my_list)
result = reduce(lambda prev, cur: prev * cur, my_list)
print(result)
