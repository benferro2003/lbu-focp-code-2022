#!/usr/bin/env python3


if __name__ == '__main__':

    try:
        times_table = int(input('What table do you want to see? '))

        if 0 <= abs(times_table) <= 12:
            if times_table >= 0:
                for line in range(13):
                    print(line, 'x', times_table, '=', line * times_table)
            else:
                for line in range(12, -1, -1):
                    print(line, 'x', abs(times_table), '=', line * abs(times_table))
        else:
            print('Sorry. Value out of range.')
    except ValueError:
        print('Sorry. Need an integer there.')
