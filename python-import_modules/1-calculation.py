#!/usr/bin/python3
import calculator_1
a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} + {} = {}".format(a, b, sub(a, b)))
    print("{} + {} = {}".format(a, b, div(a, b)))
    print("{} + {} = {}".format(a, b, mul(a, b)))
