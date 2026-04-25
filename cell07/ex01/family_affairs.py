#!/usr/bin/env python3

def find_the_redheads(family_dict):
    
    redheads_filter = filter(lambda name: family_dict[name] == "red", family_dict)
    
    return list(redheads_filter)

def main():
    
    dupont_family = {
        "florence": "red",
        "gary": "blond",
        "virginie": "red",
        "françois": "brown"
    }
    
    print(find_the_redheads(dupont_family))

if __name__ == "__main__":
    main()