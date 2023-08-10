import sys
input = sys.stdin.readline

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if not self.empty() else -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 0 if self.stack else 1

    def top(self):
        return self.stack[-1] if not self.empty() else -1
    

n = int(input())
stack = Stack()
for i in range(n):
    order = input().split()
    if order[0] == "push":
        stack.push(order[1])
        continue
    print(getattr(stack,order[0])())