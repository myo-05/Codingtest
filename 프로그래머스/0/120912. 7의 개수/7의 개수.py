def solution(array):
    return sum(map(lambda num:str(num).count('7'), array))