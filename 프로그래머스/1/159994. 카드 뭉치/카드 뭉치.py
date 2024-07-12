def solution(cards1, cards2, goal):
    index1 = index2 = 0

    for word in goal:
        if word in cards1:
            if cards1.index(word) != index1:
                return "No"
            else:
                index1 += 1
        else:
            if cards2.index(word) != index2:
                return "No"
            else:
                index2 += 1
    return "Yes"