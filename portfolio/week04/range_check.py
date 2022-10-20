#!/usr/bin/env python3

def is_between_zero_and_hundred(an_integer):
    return 0 <= an_integer <= 100


if __name__ == '__main__':
    for i in [-100, -50, -1, 0, 1, 25, 50, 75, 99, 100, 101, 125, 150, 1000]:
        print(f'{i:3} -> {is_between_zero_and_hundred(i)}')
