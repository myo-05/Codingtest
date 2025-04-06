def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers.pop())
    else:
        numbers.append(numbers.pop(0))
    answer += numbers
    return answer