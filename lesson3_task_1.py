def my_div(numb_1, numb_2):
    result = numb_1 / numb_2
    return result


number_1 = int(input('Enter the 1 number -  '))
number_2 = int(input('Enter the 2 number -  '))
if number_2 != 0:
    my_result = f'{my_div(number_1, number_2):.2f}'
    print(my_result)
else:
    print("You can't divide by 0 ")
