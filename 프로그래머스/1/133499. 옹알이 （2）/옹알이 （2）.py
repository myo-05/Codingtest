'''
["aya", "ye", "woo", "ma"]
네 가지 발음 조합만 가능
연속발음 불가
문자열 리스트 babbling input
발음가능 단어 reuturn
'''
def solution(babbling):
    babbling_list = ["aya", "ye", "woo", "ma"] # 발음가능 리스트
    count = 0 # 발음가능 단어 수
    for babbles in babbling: # 문자열 순회
        tmp1 = "" # 철자 저장
        tmp2 = "" # 이전 옹알이 저장
        for s in babbles: # 옹알이 철자 순회
            tmp1 += s # 철자를 하나씩 추가
            if tmp1 != tmp2 and tmp1 in babbling_list: # 이전 옹알이가 아니면서, 발음 가능하다면
                tmp2 = tmp1 # 현재 옹알이 저장
                tmp1 = "" # 철자 초기화
        if tmp1 == "": # 모든 옹알이를 했다면
            count += 1
    return count