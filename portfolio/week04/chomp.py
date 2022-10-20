#!/usr/bin/env python3

def chomp(s):
    return s[:-1] if len(s) > 1 else s


if __name__ == '__main__':
    for s in ['cheesey', '123456', 'Ni', 'spam', '', 'A']:
        print(f'"{s}" -> "{chomp(s)}"')
