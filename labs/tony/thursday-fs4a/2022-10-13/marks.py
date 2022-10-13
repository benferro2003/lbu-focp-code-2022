#!/usr/bin/env python3

from statistics import mean


if __name__ == '__main__':

    NUMBER_OF_MARKS = 5

    marks = []

    while True:
        try:
            mark = int(input(f'Enter mark #{len(marks) + 1}: '))

            if 0 <= mark <= 100:
                marks.append(mark)
                if len(marks) == NUMBER_OF_MARKS:
                    break
            else:
                print('Mark out of range!')
        except ValueError:
            print('Error. Value is not a valid mark.')

    max_mark = max(marks)
    min_mark = min(marks)
    avg_mark = mean(marks)

    print()

    print('Highest Mark:  ', max_mark)
    print('Lowest Mark:   ', min_mark)
    print('Average Mark:  ', avg_mark)
