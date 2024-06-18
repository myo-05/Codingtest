def solution(s):
    s_len = len(s)
    mid_index = s_len//2
    return s[mid_index-1:mid_index+1] if s_len % 2 == 0 else s[mid_index]