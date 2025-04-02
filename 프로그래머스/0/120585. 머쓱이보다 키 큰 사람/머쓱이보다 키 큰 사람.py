def solution(array, height):
    return sum(int(h > height) for h in array)