#!/usr/bin/env python3

import sys

user_input = input("Enter a number: ")

try:
    
    num = float(user_input)
    
    if num == int(num):
        print("The entered number is an integer.")
    else:
        print("The entered number is a decimal.")

except ValueError:
    print("Error: That is not a valid number.")
    sys.exit()