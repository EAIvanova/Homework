dic_subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.replace('-', '0').replace(':', '')\
            .replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').split()
        dic_subj[line[0]] = sum(map(int, line[1:]))
    print(f'Общее количество часов по предметам:\n{dic_subj}')
