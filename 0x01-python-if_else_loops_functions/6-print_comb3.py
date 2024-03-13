#!/usr/bin/python3
for i in range(1, 10):
  for j in range(i, 10):
        print("{:02d}, ".format(i + j), end='')
print("{:02d}".format(i * 10 + j, 89))

