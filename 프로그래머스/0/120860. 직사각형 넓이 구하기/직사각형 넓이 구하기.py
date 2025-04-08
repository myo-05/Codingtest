def solution(dots):
    answer = 0
    x = list(set(map(lambda dot: dot[0],dots)))
    y = list(set(map(lambda dot: dot[1],dots)))
    return abs((x[0]-x[1])*(y[0]-y[1]))