def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    return int(myString.find(pat) > -1)