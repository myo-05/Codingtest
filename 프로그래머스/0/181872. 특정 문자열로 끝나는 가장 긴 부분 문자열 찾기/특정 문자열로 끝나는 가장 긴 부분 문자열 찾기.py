def solution(myString, pat):
    index = myString.rfind(pat) + len(pat)
    answer = myString[:index]
    return answer