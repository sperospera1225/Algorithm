# 2. 스택 & 큐
# 1) 스택 Min : 기본적인 push 기능과 pop 기능이 구현된 스택에서 최솟값을 반환하는 min 함수를 추가하려고 한다.
# 어떻게 설계할 수 있겠는가? push, pop, min 연산은 모두 O(1) 시간에 동작해야 한다.
class Stack():
    stack = list()
    def push(self, number):
        self.stack.append(number)
        # print(list[len(list)])
    def pop(self):
        self.stack.pop()
    def min(self):
        return min(self.stack)

# 2) 스택으로 큐 : 스택 두 개로 큐 하나를 구현한 MyQueue 클래스를 구현하라.
class MyQueue():
    stack1 = list()
    stack2 = list()

    def inQueue(self, item):
        self.stack1.append(item)
    def outQueue(self):
        if self.stack2:
            while not self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# 3) 스택 정렬 : 가장 작은 값이 위로 오도록 스택을 정렬하는 프로그램을 작성하라. 추가적으로 하나 정도의 스택은 사용해도 괜찮지만, 스택에 보관된 요소를 배열 등의 다른 자료구조로 복사할 수는 없다. 스택은 push, pop, peek, isEmpty의 네 가지 연산을 제공해야 한다.

# 4) https://www.acmicpc.net/problem/2504

quotation = input().strip()
stack = []
def calculation(quotation):
    stack = []
    for s in calculation():
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                temp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = temp * 2
                        break
                    else:
                        temp += stack[i]
                        stack = stack[:-1]
        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                temp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = temp * 3
                        break
                    else:
                        temp += stack[i]
                        stack = stack[:-1]
        else:
            return 0
    return sum(stack)
# 5) https://www.acmicpc.net/problem/10799
pipe = list(input())
result = 0
stack = []

for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append('(')
    else:
        if pipe[i - 1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
