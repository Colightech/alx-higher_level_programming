#!/usr/bin/python3
import sys

n = len(sys.argv)
print("{} arguements:".format(n - 1))
for i in range(1, n):
    print("{}: {} ".format(i, sys.argv[i]))
