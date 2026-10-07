#!/usr/bin/env python3

import sys


def shrink(string):
    print(string[:8])


def enlarge(string):
    string += "Z" * (8 - len(string))
    print(string)


arguments = sys.argv[1:]

if not arguments:
    print("none")
else:
    for argument in arguments:
        if len(argument) > 8:
            shrink(argument)
        elif len(argument) < 8:
            enlarge(argument)
        else:
            print(argument)