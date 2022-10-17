#!/usr/bin/env python3

if __name__ == '__main__':

    while True:
        table = int(input('What times table do you want to see? '))

        if 0 <= abs(table) <= 12:
            if table >= 0:
                for row in range(13):
                    print(f'{row:2} x {table} = {row * table:3}')
            else:
                for row in range(12, -1, -1):
                    print(f'{row:2} x {abs(table)} = {row * abs(table):3}')
            break
        else:
            print('Sorry. That value is out of range. Try again.')
