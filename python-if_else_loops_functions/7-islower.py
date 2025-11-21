#!/usr/bin/python3
def islower(c):
    return ord(c) >= ord("a") and ord(c) <= ord('z')
print("a => {}".format("lower" if islower('a') else "upper")
