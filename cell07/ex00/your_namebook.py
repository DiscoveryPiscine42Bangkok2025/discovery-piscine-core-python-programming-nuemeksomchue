#!/usr/bin/env python3

def array_of_names(names_dict):
    
    full_names = []
    
    for first_name, last_name in names_dict.items():
        
        
        formatted_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        
        full_names.append(formatted_name)
        
    return full_names

def main():
    
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "ada": "lovelace"
    }
    
    print(array_of_names(persons))

if __name__ == "__main__":
    main()