def solution(numLog):
    command = ''
    action = {'w':1, 's':-1, 'd':10, 'a':-10}
    reverse_action = dict(zip(action.values(), action.keys()))
    for i in range(0,len(numLog)-1):
        diff = numLog[i+1] - numLog[i] # 차이
        command += reverse_action[diff]
    
    return command