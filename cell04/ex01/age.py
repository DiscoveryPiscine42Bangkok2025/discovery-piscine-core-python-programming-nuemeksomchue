#!/usr/bin/env python3

import sys

try:
    age_str = input("Please tell me your age: ")
    age = int(age_str)
except ValueError:
    print("Error: Please enter a valid number for age.")
    sys.exit()

print(f"You are currently {age} years old.")

print(f"In 10 years, you will be {age + 10} years old.")
print(f"In 20 years, you will be {age + 20} years old.")
print(f"In 30 years, you will be {age + 30} years old.")