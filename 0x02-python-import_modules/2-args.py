#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    current = len(sys.argv) - 1

    if current == 0:

        print("0 arguments.")

    elif current == 1:

        print("1 argument:")

    else:

        print("{} arguments:".format(current))

    for i in range(current):

        print("{}: {}".format(i + 1, sys.argv[i + 1]))
