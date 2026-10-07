#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    z_characters = [character for character in sys.argv[1] if character == "z"]
    if z_characters:
        print("".join(z_characters))
    else:
        print("none")