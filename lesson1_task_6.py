km_s = int(input("Введи количество км, которое спортсмен пробежал в 1 день - "))
km_f = int(input("Введи количество км, которое спортсмен должен пробегать - "))

counter = 1

if km_f < km_s:
    print("Второе число должно быть больше первого.")

elif km_f == km_s:
    print(" 1 день ")

else:
    while km_s < km_f:
        km_s = km_s + (km_s * 0.1)
        counter += 1
        if km_s >= km_f:
           result = f'На {counter} день спортсмен достиг результата не менее {km_f} км в день'

           print(result)























