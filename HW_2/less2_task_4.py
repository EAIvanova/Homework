
my_str = str(input("Введи несколько слов, разделенных пробелами -  "))
print(my_str)

my_str_2 = my_str.split()
counter = 0

for my_word_2 in my_str_2:
    print(counter + 1, my_word_2[:10])
    counter += 1
