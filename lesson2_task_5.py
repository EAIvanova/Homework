my_list = [20, 17, 12, 12, 7, 4]
number = int(input("Введи новый элемент рейтинга -  "))
q = len(my_list)
counter = 0
if number <= my_list[q - 1]:
    my_list.insert(q, number)
    print(my_list)
else:
    for new_elem in my_list:
        if new_elem >= number:
            counter += 1
        elif number > new_elem:
            my_list.insert(counter, number)
            print(my_list)
            break
