#!/usr/bin/env python3

def c2f(c):
    return c * 9 / 5 + 32


def f2c(f):
    return (f - 32) * 5 / 9


if __name__ == '__main__':

    for c in range (-20, 40, 5):
        print(f'{c:3}C -> {c2f(c):>6.2f}F')

        print()

        for f in range(20, 90, 5):
            print(f'{f:3}F -> {f2c(f):>6.2f}C')
