#!/usr/bin/python3
"""class square: optional size must be int."""


class Square:
    """takes size int and greater than or equal to zero"""
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        self.__size = size
