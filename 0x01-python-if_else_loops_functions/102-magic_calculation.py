#!/usr/bin/pytho3
# lo2-magic_calculation.py

def magic_calculation(a, b, c):
    """Matching bytecode provided by Holberton School"""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
