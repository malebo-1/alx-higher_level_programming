#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Finds multiples of 2 in list"""
    multiples = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
