import string
def solution(my_string):
    answer = []
    dict_alpha=string.ascii_uppercase+string.ascii_lowercase
    for i in dict_alpha:
        x= my_string.count(i) if i in my_string else 0
        answer.append(x)
    return answer