#!/usr/bin/python3
def print_list_integer(my_list=[]):
    list_len = len(my_list)
    for x in range(0, list_len):
        print("{:d}".format(my_list[x]))
