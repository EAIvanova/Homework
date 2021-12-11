from sys import argv


script_name, a, b, c = argv
print('Выработка в часах: ', a)
print('Ставка в часах: ', b)
print('Премия: ', c)
vir_h = int(argv[1])
st_h = int(argv[2])
prem = int(argv[3])
print('Итоговая ЗП: ', vir_h * st_h + prem)
