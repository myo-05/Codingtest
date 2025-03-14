def solution(myString):
    for s in myString:
        if s<'l':
            myString = myString.replace(s,'l')
    return myString