#!/usr/bin/python3
def uppercase(str):
    result=""
    for l in str:
        if ord('a') <= ord(l) <= ord('z'):
            result += l
        else: 
            u = ord(l) + 32
            result += chr(u)
    return result
print(uppercase('ABAHA'))"
