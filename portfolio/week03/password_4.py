#!/usr/bin/env python3

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']


if __name__ == '__main__':

    while True:
        password = input('Enter your new password:   ')
        check = input('Re-enter the same password:')

        if password == check and len(password) >= 8 and len(password) <= 12 and password not in BAD_PASSWORDS:
            print('Password Set')
            break
        else:
            print('Error. Passwords do not match.')
        