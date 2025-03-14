def solution(date1, date2):
    for d1,d2 in zip(date1,date2):
        if d1<d2:
            return 1
        elif d1>d2:
            break
    return 0