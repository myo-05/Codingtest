def solution(array, n):
    d = 0
    while True:
        for i in sorted(array):
            if abs(i-n)==d:
                return i
        d += 1