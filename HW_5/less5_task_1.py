with open('text_1.txt', 'w', encoding='utf-8') as f:

    while True:
        line = input('Enter your text: ')
        if not line:
            break
        print(line, file=f)
