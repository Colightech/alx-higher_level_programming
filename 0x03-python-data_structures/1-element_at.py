#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    if idx < 0 or idx > list_len - 1:
        return (0)
    return (my_list[idx])
