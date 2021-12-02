list_1 = []
otv = 'n'
while otv == 'n':

    el_list = input("Введи элемент списка - ")
    list_1.append(el_list)
    otv = input("Ввод списка закончен? n/y  ")
if otv != 'n':
    print("Ввод окончен")

result_1 = f'Ваш список   {list_1}'
print(result_1)

q = len(list_1)
list_2 = []
if q == 1:
    print("Ваш список не изменился")
elif q > 1:
    counter = 0
    q_1 = q % 2
    if q_1 == 0:
        while counter <= q - 1:
            list_2.append(list_1[counter + 1])
            list_2.append(list_1[counter])
            counter += 2
        result_2 = f'Новый список   {list_2}'
        print(result_2)
    if q_1 != 0:
        while counter <= q - 2:
            list_2.append(list_1[counter + 1])
            list_2.append(list_1[counter])
            counter += 2
        list_2.append(list_1[q - 1])
        result_2 = f'Новый список   {list_2}'
        print(result_2)
