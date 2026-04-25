#!/usr/bin/env python3

def main():
    
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    filtered_list = [x + 2 for x in original_array if x > 5]

    unique_list = list(set(filtered_list))

    print(original_array)
    print(unique_list)

if __name__ == "__main__":
    main()