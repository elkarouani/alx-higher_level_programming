#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    keys_list = list(new_dict.keys())

    for i in keys_list:
        new_dict[i] *= i
    return new_dict
