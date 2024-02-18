#!/usr/bin/python3

"""a function that divides 2 integers and prints the result."""


def safe_print_division(a, b):
    """Returns the value of the division, otherwise: None.
    Args:
        value(int): a (numerator)
                    b (denomenator)
    Raises:
        ZeroDivisionError (if b is zero)
    """
    try:
        div = a / b
    except(ZeroDivisionError):
        div = None
    finally:
        print("Inside result:{}".format(div))
        return (div)
