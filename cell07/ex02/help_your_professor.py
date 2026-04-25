#!/usr/bin/env python3

def average(class_scores):
    
    if not class_scores:
        return 0
    
    scores = class_scores.values()
    
    total_sum = sum(scores)
    
    avg = total_sum / len(class_scores)
    
    return avg

def main():
    
    class_6A = {
        "jean": 15,
        "ada": 18,
        "grace": 17,
        "louis": 12
    }
    class_6B = {
        "alex": 10,
        "bob": 15,
        "charlie": 20
    }
    print(f"Average for class 6A: {average(class_6A)}")
    print(f"Average for class 6B: {average(class_6B)}")

if __name__ == "__main__":
    main()