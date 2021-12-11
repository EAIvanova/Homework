from itertools import cycle, count


a = int(input('Enter the First number:  '))
b = int(input('Enter the Last number:  '))
c = b - a + 1

my_counter = count(a)
for i in range(c):
    print(next(my_counter), end=' ')

x = int(input('Enter number of repetitions:  '))
my_list = [1, 'w', 4, 't', 7, 'z']

my_cycle = cycle(my_list)
for i in range(x):
    print(next(my_cycle), end=' ')
