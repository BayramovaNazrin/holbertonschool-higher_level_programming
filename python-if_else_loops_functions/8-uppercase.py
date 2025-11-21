#!/usr/bin/python3
def uppercase(str):
    result=""
    for l in str:
        if ord('a') <= ord(l) <= ord('z'):
            result += chr(ord(l) - 32)
        else: 
            result += l
    print("{}".format(result))
