#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d_sort = list(a_dictionary.keys())
    d_sort.sort()
    for x in d_sort:
        print("{}: {}".format(x, a_dictionary.get(x)))
