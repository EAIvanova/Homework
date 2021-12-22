from random import randint
my_list = []

for i in range(14):
    result = randint(1, 50)
    my_list.append(result)
print(my_list)

my_list_3 = [x for x in my_list if my_list.count(x) == 1]
print(my_list_3)
