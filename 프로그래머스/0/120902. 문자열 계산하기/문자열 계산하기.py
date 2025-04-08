def solution(my_string):
    return sum(map(lambda s : int(s) , my_string.replace(' - ',' + -').split(' + ')))