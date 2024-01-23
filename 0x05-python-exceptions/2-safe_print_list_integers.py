#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """This prints the x element that first appears on the int list.

    Arguements:
        my_list (list): The list to print from.
        x (int): The no. of elements of my_list to print.

    Returns:
        The no. of elements to be printed.
    """
    returns = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            returns += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (returns)
