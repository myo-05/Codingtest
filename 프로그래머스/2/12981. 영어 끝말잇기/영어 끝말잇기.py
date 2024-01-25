def solution(n, words):
    # 탈락이 발생할 경우 판별
        # 1) 중복된 단어가 있을 경우
        # 2) 단어가 이어지지 않을 경우
    # 탈락하는 사람의 번호 판별
    # 탈락하는 순간 순회한 횟수 판별
    # 탈락자 생기지 않을 경우 [0,0] 리턴
        # 중복단어 없고, 단어가 모두 이어질 때
    
    words_ = words[:-1] # 마지막 단어 제외한 리스트
    for i,word in enumerate(words_,1):# 1부터 시작
        # 단어가 이어지지 않거나, 중복되면 탈락 
        if word[-1] != words[i][0] or words[:i+1].count(words[i])>1:
            # 탈락하는 사람의 번호
            loser_num = n if (i+1)%n == 0 else (i+1)%n
            # 탈락하는 순간 순회한 횟수
            lose_turn = (i+1)//n if (i+1)%n == 0 else (i+1)//n+1
            return [loser_num,lose_turn]
    return [0,0] # 탈락자 생기지 않는다