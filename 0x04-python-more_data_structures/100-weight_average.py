#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight_score = 0
    factor = 0

    for record in my_list:
        weight_score += record[0] * record[1]
        factor += record[1]

    return weight_score / factor
