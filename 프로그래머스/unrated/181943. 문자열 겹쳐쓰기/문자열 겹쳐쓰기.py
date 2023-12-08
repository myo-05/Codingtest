def solution(my_string, overwrite_string, s):
    N = len(overwrite_string)
    a = my_string[:s]
    b = overwrite_string
    c = my_string[s+N:]
    return a+b+c
    
    