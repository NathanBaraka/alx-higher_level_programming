#!/usr/bin/python3
if __name__ =="__main__":
    from sys import argv
    x = len(argv) -1
    if x < 1:
        print(f"{x} arguments.")
    elif x == 1:
        print(f"{x} argument:")
    else:
        print(f"{x} arguments:")

        for i in range(x):
            print("{}: {:s}".format(i + 1, argv[i + 1]))
