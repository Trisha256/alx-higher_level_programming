#!/usr/bin/python3
"""Defines print name function."""


def say_my_name(first_name, last_name=""):
    """
    Prints a name.

    Args:
        first_name(str): first name to print.
        second_name(str): second name to print.

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
