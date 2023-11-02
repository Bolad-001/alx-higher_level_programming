#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition all argument"""
    import sys

    add_tot = 0
    argument = sys.argv[1:]
    add_tot += sum(int(i) for i in argument)

    print('{}'.format(add_tot))
