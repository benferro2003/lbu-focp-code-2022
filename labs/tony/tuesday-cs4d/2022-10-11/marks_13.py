#!/usr/bin/env python3

from statistics import mean as avg, median, stdev


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
        print(f'Highest Mark:   {max(marks)}')
        print(f'Lowest Mark:    {min(marks)}')
        print(f'Average Mark:   {avg(marks):.2f}')
        print(f'Median Mark:    {median(marks):.2f}')
        print(f'Standard Devn:  {stdev(marks):.2f}')

    except ValueError:
        print('No marks entered. Nothing to do.')
