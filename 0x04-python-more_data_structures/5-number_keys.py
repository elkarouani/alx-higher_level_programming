#!/usr/bin/python3

def number_keys(a_dictionary):
    count = 0
    for i in list(a_dictionary.keys()):
        count += i
    return count
