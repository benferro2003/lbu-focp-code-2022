#!/usr/bin/env python3

from marks import avg

if __name__ == '__main__':

    print(avg([1, 2, 3, 4]))
    try:
        print(avg(['a', 'b']))
        print(avg([]))
    except TypeError:
        print('Cannot find average of something that is not a number.')
    except ZeroDivisionError:
        print('Cannot find average of an empty list.')
