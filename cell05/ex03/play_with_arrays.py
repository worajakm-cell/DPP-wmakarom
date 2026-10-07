#!/usr/bin/env python3
array1 = [2,4,6,8,10,12,8,6]
array2 = [x + 2 for x in array1 if x > 5]
set = set(array2)
print(array1)
print(set)