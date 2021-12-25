with open('text_3.txt') as file:
    file_lines = file.readlines()
    dict_pers = {}
    sum_zp = 0
    for line in file_lines:
        pers_info = line.split()
        dict_pers.update({pers_info[0]: float(pers_info[1])})
        sum_zp += float(pers_info[1])
average_zp = sum_zp / len(dict_pers)
print(f'Average = {average_zp:.2f}')

for k, v in dict_pers.items():
    if v < 20000:
        print(f'{k}: {v}')
