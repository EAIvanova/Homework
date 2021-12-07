def my_func(x, y):
    if x > 0 and y < 0:
        y_1 = abs(y)
        z = 1
        for i in range(y_1):
            z *= x
        result = f'{(1 / z):.4f}'
        return result


number_1 = float(input('Enter the 1 number (real positive) -  '))
number_2 = int(input('Enter the 2 number (negative integer) -  '))
if number_1 < 0:
    print("You must enter the positive number.")
if number_2 > 0:
    print("You must enter the negative integer")
else:
    my_result_2 = f'{(number_1 ** number_2):.5f}'
    print(my_result_2)
my_result = my_func(number_1, number_2)
print(my_result)
