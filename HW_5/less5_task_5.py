from random import randint


with open('text_5.txt', 'w', encoding='utf-8') as file:
    my_list = [randint(1, 30) for _ in range(30)]
    file.write(''.join(map(str, my_list)))

result = sum(my_list)
print(my_list)
print(result)
