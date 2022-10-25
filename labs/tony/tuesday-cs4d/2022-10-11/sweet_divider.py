#!/usr/bin/env python3
if __name__ == '__main__':
    print('Checkpoint task 2 - BEN FERRO')
    slices = int(input('How many slices of spam one requires?'))
    while slices < 1:
        slices = int(input('How many slices of spam one requires?'))

    spam = 'spam, '
    print(f'Egg with {spam*(slices-1) + "and spam coming up" if slices > 1 else"spam coming up!"}')
