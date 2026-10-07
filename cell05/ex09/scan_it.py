#!/usr/bin/env python3
import re
import sys

if len(sys.argv) != 3:
    print("none")
else:
    matches = re.findall(re.escape(sys.argv[1]), sys.argv[2])
    if matches:
        print(len(matches))
    else:
        print("none")