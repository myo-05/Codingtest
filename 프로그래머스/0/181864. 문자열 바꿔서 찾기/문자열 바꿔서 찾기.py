def solution(myString, pat):
    answer = 0
    myString_trans = ''.join('B' if s == 'A' else 'A' for s in myString)
    return int(myString_trans.find(pat)>-1)