#!/usr/bin/env python3

def count_letters(a_string):
    upper = lower = 0

    for letter in a_string:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    return lower, upper


if __name__ == '__main__':
    for s in ['cheese', 'Cheese', 'CHEESE', 'ChEeSeY', 'cheeseIness', 'ch33se', '123456']:
        print(f'{s:12} -> Lower: {count_letters(s)[0]:2} Upper: {count_letters(s)[1]:2}')
