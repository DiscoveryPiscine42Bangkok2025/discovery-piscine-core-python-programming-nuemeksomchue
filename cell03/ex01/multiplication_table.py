#!/usr/bin/env python3

import sys

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
    sys.exit()

i = 0
while i < 10:
    result = i * number
    print(f"{i} x {number} = {result}")
    i += 1