#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments")
    else:
        if num_arguments == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(num_arguments))

        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
