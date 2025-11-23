#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)-1
    if a == 1:
        print("{} argument:".format(a))
    elif a == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(a))
    for i in range(1, a+1):
        print("{}: {}".format(i, sys.argv[i]))
