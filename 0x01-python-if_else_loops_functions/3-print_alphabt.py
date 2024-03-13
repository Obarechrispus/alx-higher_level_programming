#!/usr/bin/python3
for i in range(ord('a'), ord('z') +1):
    if chr(i) != 'q' and chr(i) != 'z':
        print("{}".format(chr(i)), end='')
