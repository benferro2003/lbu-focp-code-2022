#!/usr/bin/env python3

from statistics import mean as avg


if __name__ == '__main__':

    marks = []

    while True:
        try:
            mark = input(f'Enter next mark: ')
            if not mark:
                break

            if 0 <= int(mark) <= 100:
                marks.append(int(mark))
            else:
                print('Error: Value is out of range.')
        except ValueError:
            print('Error: Value is not an integer.')

    try:
        max_mark = max(marks)
        min_mark = min(marks)
        avg_mark = avg(marks)

        print(f'Highest Mark: {max_mark}')
        print(f'Lowest Mark:  {min_mark}')
        print(f'Average Mark: {avg_mark:.2f}')

    except ValueError:
        print('No marks entered. Nothing to do.')
