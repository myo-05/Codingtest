def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0: #만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
            stk.append(arr[i])
            i += 1
        else:
        # stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
        # stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.   
            else:
                stk.pop()
    return stk