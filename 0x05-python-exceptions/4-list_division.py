#!/usr/bin/python3

"""a function that divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    """Returns a new list (length = list_length) with all divisions.
    Args:
        my_list_1: numerator
        my_list_2: denomenator
        list_length: length of the string
    Raises:
        TypeError: element is not an integer or float
        ZeroDivisionError: /0
        IndexError: list is too short
    """
    result_list = []
    for i in range(list_length):
        try:
            val_1 = my_list_1[i]
            val_2 = my_list_2[i]

            result = val_1 / val_2
            if not isinstance(val_1, (int, float)) or not isinstance(val_2,
(int, float)):
                print("wrong type")
                if val_2 == 0:
                    raise ZeroDivisionError("division by 0")
        except (ZeroDivisionError):
            print("division by 0")
            result = 0
        except (TypeError):
            print("wrong type")
            result = 0
        except (IndexError):
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
