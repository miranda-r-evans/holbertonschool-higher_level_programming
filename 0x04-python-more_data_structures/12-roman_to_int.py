#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is not True:
        return 0
    sum = 0
    biggest_val = 1
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                  'D': 500, 'M': 1000}
    for let in roman_string:
        if let not in roman_dict:
            return 0
        if roman_dict[let] > biggest_val:
            biggest_val = roman_dict[let]
            sum = roman_dict[let] - sum
        else:
            sum = sum + roman_dict[let]
    return sum
