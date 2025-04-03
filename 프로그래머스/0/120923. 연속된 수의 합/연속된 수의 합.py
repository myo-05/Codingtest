def solution(num, total):
    start = total//num - num//2
    Sum = sum(i for i in range(start,start+num))
    while Sum < total:
        start += 1
        Sum = sum(i for i in range(start,start+num))
    return list(i for i in range(start,start+num))