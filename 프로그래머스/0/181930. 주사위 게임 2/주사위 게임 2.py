def solution(a, b, c):
    case = [(a + b + c),(a**2+b**2+c**2),(a**3+b**3+c**3)]
    if len(set([a,b,c])) == 3 : # 세 숫자가 모두 다르다면 a + b + c 점
        return case[0]
    if len(set([a,b,c])) == 2 : # 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점
        return case[0]*case[1]
    if len(set([a,b,c])) == 1 : # 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점
        return case[0]*case[1]*case[2]
        