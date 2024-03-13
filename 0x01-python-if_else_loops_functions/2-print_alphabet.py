#!/usr/bin/python3
print(''.join('{}' for _ in range(ord('a'), ord('z') + 1)).format(*(chr(i) for i in range(ord('a'), ord('z') + 1))))

