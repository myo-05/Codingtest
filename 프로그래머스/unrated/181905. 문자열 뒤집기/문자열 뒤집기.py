def solution(my_string, s, e):
    
    l = len(my_string) 
    str_left = my_string[:s]
    str_middle = my_string[s:e+1][::-1]
    str_right = my_string[e+1:]
    
    answer = str_left + str_middle + str_right 

    return answer