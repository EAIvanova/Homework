name = input("Введи свое имя - ")
print("Привет, " + name + "!")
number = int(input("Введи количество секунд, а я переведу их в формат чч:мм:сс - "))

if number < 3600:
    if number < 60:
        result = f"00:00:{number:02}"
        print(result)
    else:
        number >= 60 and number < 3600
        number_min = number // 60
        number_sec = number % 60
        result = f"00:{number_min:02}:{number_sec:02}"
        print(result)

else:
    number >= 3600
    number_h = number // 3600
    number_r = number % 3600
    number_min = number_r // 60
    number_sec = number_r % 60
    result = f"{number_h:02}:{number_min:02}:{number_sec:02}"
    print(result)
















