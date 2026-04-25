#!/usr/bin/env python3
import sys

def main():
    
    params = sys.argv[1:]
    
    if not params:
        
        print("none")
        return

    
    for p in params:
    
        if p.endswith("ism"):
            
            continue
        
        print(f"{p}ism")

if __name__ == "__main__":
    main()