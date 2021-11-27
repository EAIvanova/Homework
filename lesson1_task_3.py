name = input("Введи свое имя - ")
print("Привет, " + name + "!")
number = str(input("Введи число n, а я вычислю выражение n + nn +nnn:  - "))

number_sec = number * 2
number_thd = number * 3

result = int(number) + int(number_sec) + int(number_thd)
result_f = f"{number} + {number_sec} + {number_thd} = {result}"

print(result_f)









