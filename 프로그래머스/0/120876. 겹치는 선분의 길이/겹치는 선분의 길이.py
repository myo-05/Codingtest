def solution(lines):
    n = len(lines)
    # 집합화
    line_set = list(map(lambda l : set(i for i in range(l[0],l[1])),lines))
    # 교차점 계산
    intersections = []
    for i in range(n):
        for j in range(i+1,n):
            intersections.append(line_set[i] & line_set[j])
    # 중복값 제외
    answer = set()
    for intersection in intersections:
        answer.update(intersection)
    return len(answer)