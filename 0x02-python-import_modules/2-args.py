#!/usr/bin/python3
if __name__ == "__main__":
    import sys

args_count = len(sys.argv) - 1
if args_count == 0:
    print("0 arguments.")
elif args_count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(args_count))
for i in range(args_count):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
