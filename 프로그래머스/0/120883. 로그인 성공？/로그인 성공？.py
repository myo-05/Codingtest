def solution(id_pw, db):
    answer = ['login','fail','wrong pw']
    if id_pw in db:
        return answer[0]
    elif id_pw[0] not in map(lambda x: x[0],db):
        return answer[1]
    else:
        return answer[2]