#!/usr/bin/python3
def no_c(my_string):
    temp_string = [z for z in my_string if z != 'c' and z != 'C']
    return ("".join(temp_string))
