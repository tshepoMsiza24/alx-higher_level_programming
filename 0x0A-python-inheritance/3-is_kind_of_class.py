#!/usr/bin/python3
# 3-is_kind_of_class.py
""" File name : 3-is_kind_of_class.py
    It is not allowed to import any module
"""


def is_kind_of_class(obj, a_class):
    """Define if a obj is instance of class"""
    if isinstance(obj, a_class):
        return True
    return False
