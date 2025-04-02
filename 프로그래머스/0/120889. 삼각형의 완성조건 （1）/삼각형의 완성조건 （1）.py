def solution(sides):
    return 2-int(sum(sides)-max(sides) > max(sides))