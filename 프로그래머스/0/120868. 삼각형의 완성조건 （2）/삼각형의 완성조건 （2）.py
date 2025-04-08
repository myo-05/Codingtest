def solution(sides):
    answer = []
    for i in range(1,sum(sides)):
        # 가장 긴 변일 경우 - 합보다 작게 / 아닐 경우 - 합이 더 크도록
        if any([i>=max(sides) and i<sum(sides), i<max(sides) and i+min(sides)>max(sides)]):
            answer.append(i)
    return len(answer)