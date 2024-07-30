'''
현재 순위 list : players
호명 명단 list : callings
경주 진행중 1등인 선수의 이름은 불리지 않습니다.
'''
def solution(players, callings):
    index_dict={p : i for i,p in enumerate(players)}
    for call in callings: # 호명 명단 순회
        i = index_dict[call] # 호명자 위치
        index_dict[call] -= 1 # 호명자 순위상승
        index_dict[players[i-1]] += 1 # 앞선수 순위하락

        players[i-1],players[i] = players[i],players[i-1] # 호명자와 앞선수 자리교체
        
    return players # 순위 반환