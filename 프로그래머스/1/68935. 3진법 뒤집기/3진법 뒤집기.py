def solution(n):
    result = ""
    while n:
        n,y=divmod(n, 3)
        result += str(y)
    return int(result, 3)