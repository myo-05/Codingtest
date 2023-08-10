import sys
input = sys.stdin.readline
n = int(input())

numbers = [i for i in range(n,0,-1)] # n부터 2까지의 배열, pop으로 추출, stack에 넣는 순서 결정
stack = [] # push (+) 시 추가
array = [] # pop (-) 시 추가
answer = []
check = True
for _ in range(n):
    num = int(input())
    while check:
        if stack == [] or stack[-1] < num:
            stack.append(numbers.pop())
            answer.append('+')
        elif stack[-1] == num:
            array.append(stack.pop())
            answer.append('-')
            break
        else:
            check = False
print("\n".join(answer) if check else "NO")