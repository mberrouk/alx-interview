#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    tab = []
    row = [1]
    i = 1

    tab.append(row)
    while (i < n):
        lent = len(tab[i - 1])
        row = []
        j = 0
        for j in range(lent + 1):
            if j == 0:
                row.append(1)
                continue
            elif j == lent:
                row.append(1)
                tab.append(row)
                break
            else:
                row.append(tab[i - 1][j - 1] + tab[i - 1][j])
        i += 1

    return tab
