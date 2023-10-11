#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set(my_list)
    result = 0
    for x in unique_int:
        result += x
    return (result)
