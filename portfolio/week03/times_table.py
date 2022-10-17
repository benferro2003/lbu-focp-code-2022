#!/usr/bin/env python3

if __name__ == '__main__':

    while True:
        table = int(input('What times table do you want to see? '))

        if 0 <= table <= 12:
            for row in range(13):
                print(f'{row:2} x {table} = {row * table:3}')
            break
        else:
            print('Sorry. That value is out of range. Try again.')
