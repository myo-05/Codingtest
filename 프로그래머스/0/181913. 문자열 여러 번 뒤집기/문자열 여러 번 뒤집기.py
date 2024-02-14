def solution(my_string, queries):
    answer = my_string
    for query in queries:
        s,e = query
        answer = answer[:s]+answer[s:e+1][::-1]+answer[e+1:]
    return answer