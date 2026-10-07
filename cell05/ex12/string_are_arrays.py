#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    zman = [character for character in sys.argv[1] if character == "z"]
    if zman:
        print("".join(zman))
    else:
        print("none")