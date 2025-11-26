#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    biggest = my_list[0]      # start with the first element

    for num in my_list[1:]:   # iterate from the second element
        if num > biggest:
            biggest = num

    return biggest
