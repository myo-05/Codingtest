def solution(todo_list, finished):
    answer = []
    for todo,check in zip(todo_list, finished):
        if check is False:
            answer.append(todo)
    return answer