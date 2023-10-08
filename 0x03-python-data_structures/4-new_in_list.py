#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    if idx < 0 or idx > list_len:
        return (my_list)
    temp_list = [z for z in my_list]
    temp_list[idx] = element
    return (temp_list)
