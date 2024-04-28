#!/usr/bin/python3
"""
    Generate Pascal's triangle up to the given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Parameters:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list of lists: - A list of lists of integers representing
                        Pascal's triangle.
                       - Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for line in range(1, n + 1):
        coef = 1
        row = []
        for k in range(1, line + 1):
            row.append(int(coef))
            coef = coef * (line - k) / k
        triangle.append(row)
    return triangle
