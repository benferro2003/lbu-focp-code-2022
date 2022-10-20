#!/usr/bin/env python3

from temp_converters import c2f, f2c


if __name__ == '__main__':

    for c in range(-25, 40, 5):
        print(f'{c:4}C --> {c2f(c):5}F.')

    print()

    for f in range(10, 100, 5):
        print(f'{f:4}F --> {f2c(f):6.2f}C.')
