#!/usr/bin/env python3

if __name__ == '__main__':
    password = input('Enter your new password:   ')
    check = input('Re-enter the same password:')

    if password == check and len(password) >= 8 and len(password) <= 12:
        print('Password Set')
    else:
        print('Error. Passwords do not match.')
        