def solution(s):
    s_list = list(s)
    stack = []

    if s[0] != '(' or s[-1] != ')': # 닫혀있지 않으면 거르기
        return False

    for i in s_list:
        stack.append(i)
        if stack[0] == '(' and i == ')' :
            stack.pop()
            stack.pop()
    if stack :
        return False        
    return True