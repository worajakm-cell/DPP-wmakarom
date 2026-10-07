#!/usr/bin/env python3

def plus_one(number):
    number = number + 1 
    print(f"Inside the function, number is {number}")

my_number = 5
print(f"Before calling the function, my_number is {my_number}")

plus_one(my_number)
print(f"After calling the function, my_number is {my_number}")