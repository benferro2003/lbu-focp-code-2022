#!/usr/bin/env python3

from statistics import mean


def avg(numbers):

    if len(numbers) == 0:
        raise ZeroDivisionError('No numbers in the list.')
    
    return sum(numbers) / len(numbers)

if __name__ == '__main__':

    NUMBER_OF_MARKS = 5

    marks = []

    while True:
        try:
            mark = input(f'Enter mark #{len(marks) + 1}: ')

            if not mark:
                break

            if 0 <= int(mark) <= 100:
                marks.append(int(mark))
            else:
                print('Mark out of range!')
        except ValueError:
            print('Error. Value is not a valid mark.')

    try:
        max_mark = max(marks)
        min_mark = min(marks)
        avg_mark = mean(marks)

        print()

        print('Highest Mark:  ', max_mark)
        print('Lowest Mark:   ', min_mark)
        print('Average Mark:  ', avg_mark)

    except ValueError:
        print('No data entered. Nothing to do.')
