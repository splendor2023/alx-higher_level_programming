#!/usr/bin/python3

def to_subtract(list_num):
    subtract_total = 0
    max_num = max(list_num)

    for num in list_num:
        if max_num > num:
            subtract_total += num

    return (max_num - subtract_total)


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_digits = list(roman_nums.keys())

    total = 0
    last_roman_num = 0
    num_list = [0]

    for char in roman_string:
        for roman_num in roman_digits:
            if roman_num == char:
                if rom_num.get(char) <= last_roman_num:
                    total += to_subtract(num_list)
                    num_list = [rom_num.get(char)]
                else:
                    num_list.append(rom_num.get(char))

                last_roman_num = rom_num.get(char)

    total += to_subtract(num_list)

    return (total)
