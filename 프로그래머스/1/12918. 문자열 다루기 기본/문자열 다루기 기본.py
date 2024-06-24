def solution(s):
    if len(s) not in [4,6]:
        return False
    try:
        int(s)
    except:
        return False
    return True