def solution(str_list):
    answer = []
    for i,s in enumerate(str_list):
        if s == 'l':
            return str_list[:i]
        elif s == 'r':
            return str_list[i+1:]            
    return answer