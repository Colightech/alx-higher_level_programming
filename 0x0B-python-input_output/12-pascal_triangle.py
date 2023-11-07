#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tr = triangles[-1]
        temp = [1]
        for x in range(len(tr) - 1):
            temp.append(tr[x] + tr[x + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
