#!/usr/bin/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for n in list_ord:
        print("{}:{}".format(n, a_dictionary.get(n)))
