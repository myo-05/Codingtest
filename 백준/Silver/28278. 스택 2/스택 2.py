import sys
input = sys.stdin.readline

stack = []
num = int(input())

for i in range(num):
    order = input().split()
    if order[0] == '1':
        stack.append(order[1])
    elif order[0] == '2':
        print(stack.pop() if stack else -1)
    elif order[0] == '3':
        print(len(stack))
    elif order[0] == '4':
        print(0 if stack else 1)
    elif order[0] == '5':
        print(stack[-1] if stack else -1)