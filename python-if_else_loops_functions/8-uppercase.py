#!/usr/bin/python3
def uppercase(str):
    result=""
    for l in str:
        if ord('A') <= ord(l) <= ord('Z'):
            result += l
        else: 
            u = ord(l) - 32
            result += chr(u)
    print("{}".format(result))
