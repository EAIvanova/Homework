a = int(input("Введите выручку фирмы - "))
b = int(input("Введите издержки фирмы - "))

if a < b:
    print('Фирма сработала в убыток')

else:
    sotrud = int(input("Введите численность сотрудников фирмы - "))
    p = a - b
    r = p / a
    p_sotrud = p / sotrud
    result_p = f'Прибыль составила: {p}'
    result_r = f'Рентабельность составила: {r:.2f}'
    result_ps = f'Прибыль на 1 сотрудника: {p_sotrud:.2f}'
    print(result_p)
    print(result_r)
    print(result_ps)















