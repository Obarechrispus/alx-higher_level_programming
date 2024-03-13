#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - 32)
            print("{}".format(upper), end='')
            
        else:
            print("{}".format(char), end='')
            

