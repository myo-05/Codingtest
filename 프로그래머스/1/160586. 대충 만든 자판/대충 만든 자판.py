'''
    할당된 문자들이 순서대로 담긴 문자열배열 keymap
    입력하려는 문자열들이 담긴 문자열 배열 targets
각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return
    단, 목표 문자열을 작성할 수 없을 때는 -1을 저장합니다.
'''
def solution(keymap, targets):
    answer = []
    for target in targets:
        click = 0
        for t in target:
            index = [] # t를 작성할 수 있는 횟수의 배열  
            for key in keymap:
                i = key.find(t)+1 # i번 누르면 작성가능
                if i > 0: # 작성가능하다면
                    index.append(i) # t를 작성할 수 있는 클릭수 저장
            if index : # 작성 가능하다면
                click += min(index) # 자판을 누르는 최소횟수 저장
            else: # 작성 불가하다면
                click = -1 # -1 저장
                break # 탈출
        answer.append(click) # target의 최소 클릭수 저장
    return answer