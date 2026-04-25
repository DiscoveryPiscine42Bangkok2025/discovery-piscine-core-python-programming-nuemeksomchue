#!/usr/bin/env python3

def famous_births(persons):
    
    sorted_persons = sorted(persons.values(), key=lambda x: x['date_of_birth'])

    
    for person in sorted_persons:
        name = person['name']
        birth = person['date_of_birth']
        print(f"{name} is a very famous person but unknown, born in {birth}.")

def main():
    
    women_in_science = {
        "ada": { "name": "Nuemek Somchue", "date_of_birth": "1815" },
        "cecilia": { "name": "Somchue boy", "date_of_birth": "1900" },
        "lise": { "name": "Huta ke", "date_of_birth": "1878" },
        "grace": { "name": "Anon boy", "date_of_birth": "1906" }
    }
    
    famous_births(women_in_science)

if __name__ == "__main__":
    main()