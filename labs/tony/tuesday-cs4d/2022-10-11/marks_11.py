#!/usr/bin/env python3

from statistics import mean as avg


if __name__ == '__main__':

    NUMBER_OF_MARKS = 3

    marks = []

    while True:
        try:
            mark = int(input(f'Enter next mark: '))
            if 0 <= mark <= 100:
                marks.append(mark)
            else:
                print('Error: Value is out of range.')
        except ValueError:
            print('Error: Value is not an integer.')

        if len(marks) == NUMBER_OF_MARKS:
            break

    max_mark = max(marks)
    min_mark = min(marks)
    avg_mark = avg(marks)

    print(f'Highest Mark: {max_mark}')
    print(f'Lowest Mark:  {min_mark}')
    print(f'Average Mark: {avg_mark:.2f}')
