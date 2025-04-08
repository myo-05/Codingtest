def solution(my_string):
    answer = 0
    mode = ['+','-']
    plus = True
    for s in my_string.split(' '):
        if s not in mode:
            if plus:
                answer += int(s)
            else:
                answer -= int(s)
        else:
            plus = s == '+' 
            
    return answer