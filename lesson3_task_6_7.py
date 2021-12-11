def int_func(word_sep):
    new_word = word_sep[0].upper() + word_sep[1:].lower()
    return new_word


my_string = input('Enter words separated by a space -  ')
for my_word in my_string.split(' '):
    result = int_func(my_word)
    print(result, end=' ')
