#!/usr/bin/python3

"""function that prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list.
    Args:
        x(int): represents the number of elements to print.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1
    except IndexError:
        pass
    print()
    return count
