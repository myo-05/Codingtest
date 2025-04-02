def solution(hp):
    answer = 0
    ant = [5,3,1]
    for a in ant:
        answer += hp//a
        hp = hp%a
    return answer