from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    boat = 0
    while people:
        weight = people.pop() # 가장 무거운 사람 태우기
        try:
            if limit-weight >= people[0]: # 가장 가벼운 사람이 무게여유 이하라면
                weight += people.popleft() # 추가
        except:
                pass
        weight = 0 # 무게제한 초기화
        boat += 1 # 탈출에 필요한 보트 추가
    return boat