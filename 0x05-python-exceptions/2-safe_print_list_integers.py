#!/usr/bin/python3

"""a function that prints the first x
elements of a list and only integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Returns the real number of integers printed.
    Args:
        x(int): represents the number of elements to access in my_list.
    Exceptions:
        ValueError: when x is bigger than the length my_list.
    """
    num = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                num += 1
    except (TypeError):
        pass
    print()
    return (num)
