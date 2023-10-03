#!/usr/bin/python3
for alphabet_lowercase in range(97, 123):
    if chr(alphabet_lowercase) != 'q' and chr(alphabet_lowercase) != 'e':
        print("{}".format(chr(alphabet_lowercase)), end="")
