#!/usr/bin/python3

from math import pi


def circle_area(r):
    if r < 0:
        raise ValueError("Value must be an integer")
    if type(r) == str:
        raise ValueError("Value must be an integer")
    return pi * (r ** 2)
