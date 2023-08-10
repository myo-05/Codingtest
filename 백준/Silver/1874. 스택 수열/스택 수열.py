import sys
input = sys.stdin.readline
n = int(input())

numbers = [i for i in range(n,0,-1)] # n부터 2까지의 배열, pop으로 추출, stack에 넣는 순서 결정
stack = [] # push (+) 시 추가
answer = []
check = True
for _ in range(n):
    num = int(input())
    while check:
        if stack == [] or stack[-1] < num: # 스택이 비어있거나, 타겟 숫자보다 낮게 쌓여있을 때
            stack.append(numbers.pop())
            answer.append('+')
        elif stack[-1] == num:
            stack.pop()
            answer.append('-')
            break
        else:
            check = False
print("\n".join(answer) if check else "NO")