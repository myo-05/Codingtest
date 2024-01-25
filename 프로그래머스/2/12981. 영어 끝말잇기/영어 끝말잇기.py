def solution(n, words):
    # 탈락이 발생할 경우 판별
        # 1) 중복된 단어가 있을 경우
        # 2) 단어가 이어지지 않을 경우
    # 탈락하는 사람의 번호 판별
    # 탈락하는 순간 순회한 횟수 판별
    # 탈락자 생기지 않을 경우 [0,0] 리턴
        # 중복단어 없고, 단어가 모두 이어질 때
    words_ = words[:-1]
    for i,word in enumerate(words_):
        print(word[-1],words[i+1][0])
        if word[-1] != words[i+1][0]: # 1
            return [(i+1)%n+1,(i+1)//n+1]
        elif words.count(word)>1: # 2
            j = words.index(word,i+1)
            return [j%n+1,j//n+1]
    return [0,0]