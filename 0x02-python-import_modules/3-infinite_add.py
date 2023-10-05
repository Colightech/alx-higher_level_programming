#!/usr/bin/python3
if __name__ == "__main__":
    import sys

result = 0
n = len(sys.argv)
for i in range(n - 1):
    result += int(sys.argv[i + 1])
print("{}".format(result))
