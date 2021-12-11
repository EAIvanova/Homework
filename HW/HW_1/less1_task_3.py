number = str(input("Введите целое положительное число n, а я вычислю выражение n + nn +nnn:  - "))

if number < '0':
    print("Необходимо ввести целое положительное число.")
else:
    number_sec = number + number
    number_thd = number + number + number

    result = int(number) + int(number_sec) + int(number_thd)
    result_f = f"{number} + {number_sec} + {number_thd} = {result}"

    print(result_f)
