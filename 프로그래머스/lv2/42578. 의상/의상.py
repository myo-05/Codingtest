def solution(clothes):
    answer = 1
    dict_clothes = {}
    for clothe in clothes:
        try:
            dict_clothes[clothe[1]] += 1 # 종류가 있다면, 추가
        except:
            dict_clothes[clothe[1]] = 1 # 종류가 없다면, 생성    
    for i in dict_clothes.values():
        answer *= (i+1) # 모든 경우의 수
    return answer-1 # 모든 경우의 수에서 하나도 착용하지 않았을 경우만 제외