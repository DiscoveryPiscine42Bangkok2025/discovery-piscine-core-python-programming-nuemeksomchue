#!/usr/bin/env python3

import sys

try:
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
except ValueError:
    print("Please enter valid integers.")
    sys.exit()

result = first_num * second_num

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

print(f"{first_num} x {second_num} = {result}")