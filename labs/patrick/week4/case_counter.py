#!/usr/bin/env python3

def case_counter(str):
    uppercase=lowercase=0
    for char in str:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

    return [uppercase, lowercase]

if __name__ == '__main__':
    phrase = input("Please enter a phrase. I'll count the cases: ")
    casecount = case_counter(phrase)
    print(f"Your phrase had {casecount[0]} uppercase characters")
    print(f"Your phrase had {casecount[1]} lowercase characters")
