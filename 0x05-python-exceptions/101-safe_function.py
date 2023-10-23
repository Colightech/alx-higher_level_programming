#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result_fct = fct(*args)
        return result_fct
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
