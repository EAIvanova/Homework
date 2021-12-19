number_1 = float(input('Enter the 1st number (real positive) -  '))
number_2 = int(input('Enter the 2nd number (negative integer) -  '))
if number_1 >= 0 and number_2 < 0:
    my_result_2 = f'{(number_1 ** number_2):.5f}'
    print(my_result_2)
else:
    print("You have to enter a positive number and a negative integer.")


def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'You have to enter a positive number x\n and a negative integer y.'
        else:
            result = 1
            for i in range(abs(y)):
                result /= x
            return f'{round(result, 5)}'
    except ValueError:
        return 'Numbers only'


num1 = input('Enter the 1st number (real positive) -  ')
num2 = input('Enter the 2nd number (negative integer) -  ')
print(my_func2(num1, num2))
