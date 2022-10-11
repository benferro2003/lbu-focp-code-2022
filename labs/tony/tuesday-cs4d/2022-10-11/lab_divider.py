#!/usr/bin/env python3

if __name__ == '__main__':
    students = int(input('How many students? '))
    group_size = int(input('Required group size? '))

    full_groups = students // group_size
    left_over = students % group_size

    print(f'There will be {full_groups} group{"s" if full_groups > 1 else ""} with '
          f'{left_over} student{"s" if left_over > 1 else ""} left over.')
