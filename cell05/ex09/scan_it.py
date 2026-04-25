#!/usr/bin/env python3
import sys
import re

def main():
    
    if len(sys.argv) == 3:
        keyword = sys.argv[1]
        content = sys.argv[2]
        
        matches = re.findall(re.escape(keyword), content)
        
        count = len(matches)
        if count > 0:
            print(count)
        else:
            print("none")
    else:
        
        print("none")

if __name__ == "__main__":
    main()