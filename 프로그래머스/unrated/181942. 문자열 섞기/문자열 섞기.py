def solution(str1, str2):
    answer = ""
    for s in zip(str1,str2):
        answer += s[0] + s[1]
    return answer