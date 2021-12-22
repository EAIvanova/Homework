from random import randint
my_list = []

for i in range(12):
    result = randint(1, 200)
    my_list.append(result)
print(my_list)
my_list_2 = []
x = 0
while x <= 10:
    if my_list[x+1] > my_list[x]:
        my_list_2.append(my_list[x+1])
    x += 1
print(my_list_2)

my_list_3 = [my_list[i] for i in range(1, 12) if my_list[i] > my_list[i - 1]]
print(my_list_3)
