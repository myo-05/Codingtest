def solution(name, yearning, photo):
    answer = []
    for people in photo:
        score = 0
        for person in zip(name,yearning):
            if person[0] in people: 
                score += person[1]
        answer.append(score)
    return answer