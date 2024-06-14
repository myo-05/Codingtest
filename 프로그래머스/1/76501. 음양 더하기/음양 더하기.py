def solution(absolutes, signs):
    return sum(i[0] if i[1] else -i[0] for i in zip(absolutes,signs))