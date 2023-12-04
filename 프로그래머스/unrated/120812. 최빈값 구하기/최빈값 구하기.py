def solution(array):
    dict_ = {}
    for arr in array:
        try:
            dict_[arr] += 1
        except:
            dict_[arr] = 1
    max_count = max(list(dict_.values()))
    list_ = [x for x in set(array) if (dict_)[x] == max_count]
    return list_[0] if len(list_) == 1 else -1