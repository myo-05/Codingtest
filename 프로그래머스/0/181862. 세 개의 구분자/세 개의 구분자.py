def solution(myStr):
    answer = [s for s in myStr.replace('a','c').replace('b','c').split('c') if s]
    return answer if answer else ["EMPTY"] 