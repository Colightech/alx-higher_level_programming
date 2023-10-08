#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list_len = len(my_list)
    if my_list_len == 0:
        return (None)
    max_list = my_list[0]
    for x in range(my_list_len):
        if my_list[x] > max_list:
            max_list = my_list[x]
    return (max_list)
