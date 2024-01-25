def solution(number, limit, power):
    # 각 기사 번호의 약수 개수를 구하기 → list로 저장
    # 제한수치를 초과하는 기사 판별 → list에서 추출후 변환
    # 각 기사의 공격력판별
    # 공격력 총합(=철의 무게)계산 후 출력
    
    def knight(num): # 약수의 개수 구하는 함수
        if num == 1:
            return 1
        result = 0
        for i in range(1,int(num**0.5)+1):
            if num / i == i: # 제곱근이면
                result += 1 # 1개 추가
            elif num % i == 0: # 제곱근이 아니면
                result += 2 # 2개 추가
        return result
    
    knight_num=[]
    for num in range(1,number+1):
        knight_num.append(knight(num))
    iron = 0 # 철의 무게
    for j in knight_num:
        iron += power if j > limit else j # 제한수치를 넘는다면 power로 치환하여 합산
    return iron