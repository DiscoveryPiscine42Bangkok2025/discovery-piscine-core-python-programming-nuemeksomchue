#!/usr/bin/env python3
import sys

def shrink(s):
    
    print(s[0:8])


def enlarge(s):
    
    needed = 8 - len(s)
    
    print(s + ('Z' * needed))

def main():
    
    params = sys.argv[1:]
    
    if not params:
        print("none")
        return

    for arg in params:
        length = len(arg)
        
        if length > 8:
            
            shrink(arg)
        elif length < 8:
            
            enlarge(arg)
        else:
            
            print(arg)

if __name__ == "__main__":
    main()