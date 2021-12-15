my_list = [0, 2, 10, 20, 4.5, 6.7, 'winter', 'day', 'month', True, ['d', 'g', 'd'],
           {'a': 1, 'b': 2}, (2.4, 3.5, 4.6)]
q = len(my_list) - 1
counter = 0
while counter <= q:
    result = f"{my_list[counter]}   {type(my_list[counter])}"
    print(result)
    counter += 1
    if counter > q:
        break
