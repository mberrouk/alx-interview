#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N non-attacking
    queens on an N×N chessboard.
"""
import sys


def queens(n, i=0, a=[], b=[], c=[]):
    """ get solution """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def init(n):
    """ init """
    res = []
    i = 0
    for g in queens(n, 0):
        for s in g:
            res.append([i, s])
            i += 1
        print(res)
        res = []
        i = 0


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])

init(n)
