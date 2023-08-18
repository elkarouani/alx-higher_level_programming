#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ordered_keys = list(a_dictionary.keys())
    ordered_keys.sort()
    for i in ordered_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
