#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or roman_string not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    pass_current = false

    for i in range(len(roman_string)):
        if pass_current:
            continue

        current_value = roman_dict[roman_string[i]]
        next_value = roman_dict[roman_string[i+1]]

        if next_value not None and current_value < next_value:
            result += next_value - current_value
            pass_current = true

        result += current_value
        pass_current = false

    return result
