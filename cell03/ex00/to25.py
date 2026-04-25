#!/usr/bin/env python3

import sys

try:
    num = int(input("Enter a number: "))
except ValueError:
    
    sys.exit()

if num > 25:
    
    print("Error")
else:
    
    while num <= 25:
        print(num)
        num += 1