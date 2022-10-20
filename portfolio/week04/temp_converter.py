#!/usr/bin/env python3

from temps import c2f
from chomp import chomp

if __name__ == '__main__':

    try:
        temp_c_str = input('Enter a Centigrade Temperate (end it with C): ')

        if temp_c_str.endswith(('C', 'c')):
            temp_f = c2f(float(chomp(temp_c_str)))
            print(f'{temp_c_str.upper()} is equivalent to {temp_f:.2f}F.')
        else:
            print('No "C" at the end of the input. Why not try again?')
    except ValueError:
        print('Invalid input. Why not try again?')
