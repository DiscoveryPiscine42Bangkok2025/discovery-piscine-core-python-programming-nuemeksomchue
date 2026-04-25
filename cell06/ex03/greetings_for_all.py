#!/usr/bin/env python3


def greetings(name="noble stranger"):
    
    if isinstance(name, str):
        
        print(f"Hello, {name}!")
    else:
        
        print("Error! The parameter is not a string.")

def main():
    
    greetings("Alice")           
    greetings()                  
    greetings(42)                

if __name__ == "__main__":
    main()