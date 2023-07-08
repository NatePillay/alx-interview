#!/usr/bin/python3
""" A function def that returns a list of lists of integers representing
the Pascal’s triangle of n: Returns an empty list if n <= 0
"""


def pascal_triangle(n):
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                previous_row = triangle[i - 1]
                current_row =  previous_row[j - 1] + previous_row[j]
                row.append(current_row)
        triangle.append(row)
    return triangle
