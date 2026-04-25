#!/usr/bin/env python3
import sys

def main():
    
    num_params = len(sys.argv) - 1
    
    if num_params > 0:
    
        print(f"parameters: {num_params}")
        
        
        for param in sys.argv[1:]:
            
            length = len(param)
            
            print(f"{param}: {length}")
            
    else:
        
        print("none")

if __name__ == "__main__":
    main()