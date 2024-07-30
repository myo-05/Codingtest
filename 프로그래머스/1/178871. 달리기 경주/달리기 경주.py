def solution(players, callings):
    tmp_name={}
    tmp_index={}
    for i,p in enumerate(players):
        tmp_name[p]=i
        tmp_index[i]=p
    for call in callings: # 호명 명단 순회
        index = tmp_name[call] # 호명자의 현위치
        tmp_name[call],tmp_name[tmp_index[index-1]] = tmp_name[tmp_index[index-1]],tmp_name[call] # 호명자와 앞 선수 자리교체
        tmp_index[index],tmp_index[index-1] = tmp_index[index-1],call
    answer = list(map(lambda x: x[0],sorted(tmp_name.items(),key=lambda item: item[1])))
    return answer # 순위 반환