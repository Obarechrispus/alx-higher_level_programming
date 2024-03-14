#!/usr/bin/python3
import string 
print(*list(string.ascii_uppercase), sep='')

for i in range(65, 91):
    print(chr(i), end='')
