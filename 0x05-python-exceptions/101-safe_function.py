#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except BaseException as a:
        res = None
        print("Exception: {}".format(a), file=sys.stderr)
    finally:
        return res
