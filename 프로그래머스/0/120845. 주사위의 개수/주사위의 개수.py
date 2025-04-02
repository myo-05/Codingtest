from math import prod

def solution(box, n):
    return prod(b//n for b in box)