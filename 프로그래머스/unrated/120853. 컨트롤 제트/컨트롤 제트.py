def solution(s):
    list_s = list(s)
    answer = []
    string = ""
    for i in list_s:
        if i == " " and string: # 공백을 만났을 때 string이 비어있지 않다면 추가
            answer.append(int(string))
            string = "" # string 리셋
        elif i == "Z": # 도르마무
            answer.pop()
        else: # 숫자라면 string에 축적
            string += i
    # 마지막 문자처리
    if s[-1] != "Z": # 마지막 문자가 숫자라면 string추가
        answer.append(int(string))
    return sum(answer) # 합산 출력