#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    
    try:
        printed_i = 0
        for i in range (x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i], end=" ")
                printed_i += 1
    except IndexError:
        pass
    print()
    return printed_i
