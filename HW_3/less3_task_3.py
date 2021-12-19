def my_func(numb_1, numb_2, numb_3):
    numb_min = min(numb_1, numb_2, numb_3)
    result = numb_1 + numb_2 + numb_3 - numb_min
    return result


number_1 = int(input('Enter the 1 number -  '))
number_2 = int(input('Enter the 2 number -  '))
number_3 = int(input('Enter the 3 number -  '))
print(my_func(number_1, number_2, number_3))

my_func_l = lambda arg1, arg2, arg3: (arg1 + arg2 + arg3) - min(arg1, arg2, arg3)

print(my_func_l(int(input('Enter the 1 number -  ')), int(input('Enter the 2 number -  ')),
                 int(input('Enter the 3 number -  '))))
