#!/usr/bin/python3
if __name__ == "__main__":
    """program to print and list the number of args"""

    import sys

    check_len = len(sys.argv[1:])

    if check_len == 0:
        print('{} arguments.'.format(check_len))
    elif check_len == 1:
        print('{} argument:'.format(check_len))
    else:
        print('{} arguments:'.format(check_len))
    for num in range(check_len):
        print('{}: {}'.format(num + 1, sys.argv[num + 1]))
