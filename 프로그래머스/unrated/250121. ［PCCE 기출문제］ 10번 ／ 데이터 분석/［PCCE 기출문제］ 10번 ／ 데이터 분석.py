def solution(data, ext, val_ext, sort_by):
    answer = []
    table_colum = ['code', 'date', 'maximum', 'remain']
    for i in data:
        [code, date, maximum, remain] = i
        if eval(ext) < val_ext: 
            answer.append(i)
    sorted_answer = sorted(answer,key=lambda x: x[table_colum.index(sort_by)])
    return sorted_answer