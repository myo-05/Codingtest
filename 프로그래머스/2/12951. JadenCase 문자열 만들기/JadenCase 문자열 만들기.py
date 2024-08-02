def JadenCase(x):
    return x[0].upper()+x[1:].lower()

def solution(s):
    return " ".join([JadenCase(S) if S else S for S in s.split(" ")])