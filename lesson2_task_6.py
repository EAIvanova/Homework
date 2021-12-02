my_list_1 = []
otv = 'нет'
count = 0
while otv == 'нет':
    count += 1
    my_list_in = []
    my_dict = {}
    print("Введите данные товаров ")
    name = str(input("Название: "))
    price = int(input("Цена: "))
    qt = int(input("Количество: "))
    meas = str(input("Ед.: "))
    my_dict['Название:'] = name
    my_dict['Цена:'] = price
    my_dict['Кол-во:'] = qt
    my_dict['Ед.:'] = meas
    my_list_in.append(count)
    my_list_in.append(my_dict)
    my_tuple = tuple(my_list_in)
    my_list_1.append(my_tuple)

    otv = input("Ввод списка закончен? да/нет  ")

if otv != 'нет':
    print("Ввод окончен")
print(my_list_1)
q = len(my_list_1)
my_dict_2 = {}
my_list_name = []
my_list_price = []
my_list_qn = []
my_list_meas = []

index = 0
for each_elem in my_list_1:
    my_tuple_inner = my_list_1[index]
    my_dict_inner = my_tuple_inner[1]
    my_list_name.append(my_dict_inner['Название:'])
    my_list_price.append(my_dict_inner['Цена:'])
    my_list_qn.append(my_dict_inner['Кол-во:'])
    my_list_meas.append(my_dict_inner['Ед.:'])
    index += 1

my_dict_fin = {'Название:': my_list_name, 'Цена:': my_list_price,
               'Кол-во:': my_list_qn, 'Ед.:': my_list_meas}
# for key, value in my_dict_fin.items():
#     my_dict_fin[key] = list(set(value))

print(my_dict_fin)
