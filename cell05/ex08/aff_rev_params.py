#!/usr/bin/env python3
import sys

def main():
    
    if len(sys.argv) >= 3:
        
        params = sys.argv[1:]
        
        reversed_params = params[::-1]
        
        for p in reversed_params:
            print(p)
            
    else:
        
        print("none")

if __name__ == "__main__":
    main()