#!/usr/bin/env python3


def avg(list_of_numbers):
    """
        Works out the average of the provided sequence.
    """

    return sum(list_of_numbers) / len(list_of_numbers)


if __name__ == '__main__':

    NUMBER_OF_MARKS = 3

    marks = []

    for count in range(NUMBER_OF_MARKS):
        mark = int(input(f'Enter mark #{count + 1}: '))
        marks.append(mark)

    max_mark = max(marks)
    min_mark = min(marks)
    avg_mark = avg(marks)

    print(f'Highest Mark: {max_mark}')
    print(f'Lowest Mark:  {min_mark}')
    print(f'Average Mark: {avg_mark:.2f}')
