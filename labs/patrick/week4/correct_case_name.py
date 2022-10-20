#!/usr/bin/env python3

def get_name():
    while True:
        str = input('What is your name?')
        if len(str)>0:
            break
    return str

def format_name_case(str):
    first_letter = str[0].upper()
    remaining_letters = str[1:].lower()
    return first_letter+remaining_letters

if __name__ == '__main__':
    name = get_name()
    name = format_name_case(name)
    print(f'Hello {name}')
