#!/usr/bin/env python3
import sys

def downcase_it(s):
    
    return s.lower()

def main():
    
    params = sys.argv[1:]
    
    if not params:
        print("none")
        return

    for p in params:
        
        result = downcase_it(p)
        print(result)

if __name__ == "__main__":
    main()