def sum_nums(nums_str, stop):
    nums_list = nums_str.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stop:
            break
        sum_list += int(i)
    return sum_list


stop_token = '/'
finished = False
s_end = 0
while not finished:
    nums_str_user = input('Enter numbers separated by a space: ')
    s_end += sum_nums(nums_str_user, stop_token)
    finished = stop_token in nums_str_user
    print(s_end)
