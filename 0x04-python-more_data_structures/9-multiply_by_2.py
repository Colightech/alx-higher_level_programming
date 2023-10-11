#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    key_dic = list(a_dictionary.keys())
    for x in key_dic:
        new_dic[x] *= 2
    return (new_dic)
