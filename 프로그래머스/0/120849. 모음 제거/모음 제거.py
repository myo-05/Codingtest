def solution(my_string):
    vowel = 'aeiou'
    for s in vowel:
        my_string = my_string.replace(s,'')
    return my_string