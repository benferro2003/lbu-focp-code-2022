#!/usr/bin/env python3

from statistics import mean, median


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
        max_mark = max(marks)
        min_mark = min(marks)
        avg_mark = mean(marks)

        print()

        print('Highest Mark:  ', max_mark)
        print('Lowest Mark:   ', min_mark)
        print('Average Mark:  ', round(avg_mark, 2))
        print('Median Mark:   ', median(marks))

    except ValueError:
        print('No data entered. Nothing to do. How sad.')
