from random import randint
my_list = []

for i in range(14):
    result = randint(1, 50)
    my_list.append(result)
print(my_list)


def my_func(my_list_2):
    my_list_un = []
    for n in my_list_2:
        if n in my_list_un:
            continue
        else:
            my_list_un.append(n)
    return my_list_un


print(my_func(my_list))
