nums = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


with open('text_4.txt', encoding='utf-8') as file, open('text_4new.txt', 'w', encoding='utf-8') as file_new:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        rus_num = nums.get(data[0])
        file_new.write(f'{line.replace(data[0], rus_num)}')
    # file_new.writelines([line.replace(line.split()[0], nums.get(line.split()[0])) for line in file])
