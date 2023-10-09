#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for list_ver in my_list:
            print("{:d}".format(list_ver))
