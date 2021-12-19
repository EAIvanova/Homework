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


def my_div2(n1, n2):
    try:
        n1, n2 = int(n1), int(n2)
        result = n1 / n2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "You can't divide by 0"
    return round(result, 2)


num1 = (input('Enter the 1 number -  '))
num2 = (input('Enter the 2 number -  '))
print(my_div2(num1, num2))
