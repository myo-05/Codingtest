def solution(want, number, discount):
    want_table = {}
    for w,n in zip(want,number):
        want_table[w] = n
    possible_day = 0 # 할인가능 날짜
    N = len(discount) # 할인기간
    # print("N",N)
    for s in range(N-10+1):
        # print(s)
        membership = discount[s:s+10]# 10일간 할인목록
        discount_table = {}
        for i in membership:
            try:
                discount_table[i] += 1
            except:
                discount_table[i] = 1
        for w in want:
            if w not in discount_table.keys():
                break
        else:
            for w in want:
                if want_table[w]>discount_table[w]:
                    break
            else:
                possible_day += 1
    return possible_day