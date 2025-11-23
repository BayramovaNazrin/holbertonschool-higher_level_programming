#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print(sys.argv[1:])
    a = len(sys.argv)-1
    print("{} arguments".format(a))
    for i in range(1, a+1):
        print("{}: {}".format(i, sys.argv[i]))
