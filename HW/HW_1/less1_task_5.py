a = float(input("Введите выручку фирмы - "))
b = float(input("Введите издержки фирмы - "))

if a < b:
    print('Фирма сработала в убыток')

else:
    pers = int(input("Введите численность сотрудников фирмы - "))
    p = a - b
    r = p * 100 / a
    p_pers = p / pers
    result_p = f'Прибыль составила: {p:.2f}'
    result_r = f'Рентабельность составила: {r:.2f}%'
    result_ps = f'Прибыль на 1 сотрудника: {p_pers:.2f}'
    print(result_p)
    print(result_r)
    print(result_ps)
