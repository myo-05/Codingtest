def solution(n):
    k = ""
    while n > 0:
        n,y=divmod(n, 3)
        k += str(y)
    return int(k, 3)