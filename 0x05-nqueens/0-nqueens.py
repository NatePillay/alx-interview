#!/usr/bin/python3
"""challenge of placing N non-attacking queens on an N×N chessboard"""
import sys


def noAttack(brd, ln, i):
    '''checks place is not attack by Queens'''
    for j in range(ln):
        if(brd[j] == i or brd[j] + ln - j == i or brd[j] + j - ln == i):
            return False
    return True


def fillPos(brd, ln):
    '''finds the next safe space to place the queen'''
    for i in range(len(brd)):
        if noAttack(brd, ln, i):
            brd[ln] = i
            if ln < len(brd) - 1:
                fillPos(brd, ln + 1)
            else:
                print([[i, brd[i]] for i in range(len(brd))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
brd = [-1 for i in range(n)]
fillPos(brd, 0)
