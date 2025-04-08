def solution(n):
    count = 0
    i = 1
    while count<n:
        if i%3 != 0 and '3' not in str(i):
            count += 1
        i += 1
    return i-1