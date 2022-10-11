#!/usr/bin/env python3

if __name__ == '__main__':
    sweets = int(input('How many students? '))
    pupils = int(input('Required group size? '))

    sweets_per_pupil = sweets // pupils
    left_over = sweets % pupils

    print(f'There will be {sweets_per_pupil} sweet{"s" if sweets_per_pupil > 1 else ""} for each pupil with '
          f'{left_over} sweet{"s" if left_over > 1 else ""} left over.')
