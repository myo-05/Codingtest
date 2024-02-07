def solution(n, control):
    action = {'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        n += action[i]
    return n