from sys import argv


if len(argv) < 4:
    print('Введите все данные (выработка, ставка, премия).')
else:
    script_name, a, b, c = argv
    print('Выработка в часах: ', a)
    print('Ставка в часах: ', b)
    print('Премия: ', c)
    vir_h = float(argv[1])
    st_h = float(argv[2])
    prem = float(argv[3])
    result = vir_h * st_h + prem
    print(f'Итоговая ЗП: , {result:.2f}')
