#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_add = set()
    for num in my_list:
        unique_add.add(num)
    return sum(unique_add)
