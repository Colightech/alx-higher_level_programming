#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    for x in range(0, list_len):
        if idx < 0 or idx > list_len:
            return (0)
        return (my_list[idx])
