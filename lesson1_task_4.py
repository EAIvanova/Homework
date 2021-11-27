number = int(input("Введи число - "))
max_n = 0
numb = number
while numb > 0:
    number_rest = numb % 10
    if number_rest >= max_n:
        max_n = number_rest
    numb = numb // 10
result = f'Наибольшая цифра в числе {number}: {max_n}'
print(result)



















