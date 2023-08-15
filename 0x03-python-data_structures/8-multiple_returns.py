#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """Length of string and first character returned"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

