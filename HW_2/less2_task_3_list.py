my_list = ['winter', 'spring', 'summer', 'fall']

number_mth = int(input("Enter month's number  1 - 12: "))

if number_mth == 1 or number_mth == 2 or number_mth == 12:
    result = my_list[0]
    print(result)
else:
    if number_mth == 3 or number_mth == 4 or number_mth == 5:
        print(my_list[1])

    else:
        if number_mth == 6 or number_mth == 7 or number_mth == 8:
            print(my_list[2])
        else:
            if number_mth == 9 or number_mth == 10 or number_mth == 11:
                print(my_list[3])
my_list_2 = ['winter', 'winter', 'winter', 'spring', 'spring', 'spring',
             'summer', 'summer', 'summer', 'fall', 'fall', 'fall', 'winter']

number_mth_2 = int(input("Enter month's number  1 - 12: "))

print(my_list_2[number_mth_2])
