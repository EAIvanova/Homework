def fact(number):
    my_fact = 1
    for i in range(1, number + 1):
        my_fact *= i

        yield my_fact


n = int(input('Enter an integer: '))
x = 0
for ind, el in enumerate(fact(n)):
    print(f'{ind + 1}! =  {el}')
