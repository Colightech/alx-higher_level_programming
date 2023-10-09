#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_len = len(my_list)
    multiple_2 = []
    for x in range(list_len):
        if my_list[x] % 2 == 0:
            multiple_2.append(True)
        else:
            multiple_2.append(False)
    return (multiple_2)
