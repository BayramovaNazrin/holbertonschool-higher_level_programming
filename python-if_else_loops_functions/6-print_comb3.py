#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i != j:
            if "{:d}{:d}".format(i, j) < "{:d}{:d}".format(j, i):
                print("{:d}{:d}".format(i, j),
                        end=", "  if "{:d}{:d}".format(i, j) != str(89) else "\n")
            else:
                continue
