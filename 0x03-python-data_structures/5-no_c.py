#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """All characters c and C removed from string"""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
