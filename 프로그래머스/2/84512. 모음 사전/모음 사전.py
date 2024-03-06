def solution(word):
    # A E I O U = 1 2 3 4 5
    words = " AEIOU"
    dictionary = []
    for s1 in words:
        for s2 in words:
            for s3 in words:
                for s4 in words:
                    for s5 in "AEIOU":
                        s = s1+s2+s3+s4+s5
                        s = s.replace(" ","")
                        dictionary.append(s)
    dictionary = set(dictionary)
    dictionary = list(dictionary)
    dictionary.sort()
    answer = dictionary.index(word)
    return answer+1
