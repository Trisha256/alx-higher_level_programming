#!/usr/bin/python3

"""a function that prints an integer with "{:d}".format()."""


def safe_print_integer(value):
    """a function that prints an integer with "{:d}".format().
    Args:
        value: value to be printed.
    Raises:
        ValueError: prints false.
    """
    try:
        print("{:d}".format(value))
        print()
        return (True)
    except (ValueError, TypeError):
        return (False)
