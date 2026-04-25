#!/usr/bin/env python3

import math
import sys

try:
    user_input = input("Enter a number: ")
    num = float(user_input)
except ValueError:
    print("Error: Please enter a valid number.")
    sys.exit()

rounded_num = math.ceil(num)

print(rounded_num)