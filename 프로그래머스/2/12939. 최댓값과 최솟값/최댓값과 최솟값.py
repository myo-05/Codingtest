def solution(s):
    s_list = list(map(int,s.split(" ")))
    return f'{str(min(s_list))} {str(max(s_list))}'