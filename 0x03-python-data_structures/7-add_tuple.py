#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #a, b = tuple_a[:2] if len(tuple_a) > 0 else 1
   # a1, b1 = tuple_b[:2] if len(tuple_b) > 0 else 1
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    b = tuple_a[1] if len(tuple_a) > 1 else 0
    a1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    sum_a = a + a1
    sum_b = b + b1

    return (sum_a, sum_b)
