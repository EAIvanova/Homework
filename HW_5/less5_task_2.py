with open('text_2.txt', encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line):
        num_word = len(value.split())
        print(f'The string {index + 1} contains {num_word} words')
