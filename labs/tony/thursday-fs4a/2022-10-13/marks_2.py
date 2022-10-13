#!/usr/bin/env python3

from statistics import mean, median, stdev


if __name__ == '__main__':

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
        print()

        print(f'Highest Mark: {max(marks):6}')
        print(f'Lowest Mark:  {min(marks):6}')
        print(f'Average Mark: {mean(marks):6.2f}')
        print(f'Median Mark:  {median(marks):6.2f}')
        print(f'Median Mark:  {stdev(marks):6.2f}')

    except ValueError:
        print('No data entered. Nothing to do. How sad.')
