#!/usr/bin/python3
"""Module for pascal_triangle function"""


def pascal_triangle(n):
    """Return Pascal's triangle as a list of lists of integers."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)] + [1]
        triangle.append(row)

    return triangle
