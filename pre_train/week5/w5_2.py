#1 TOP
n = int(input())
top = list(map(int,input().split()))
stack = []
result = []

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:  # [-1][1] 이므로 stack 맨 끝쪽에서 1번째 배열에서 1번째 데이터를 top[i]와 비교
            result.append(stack[-1][0] + 1)  # 배열은 0번째부터, 수신탑은 1번부터 시작하므로 수를 맞춰주고 result에 데이터 추가하기
            break
        stack.pop()  # 배열의 맨 끝 데이터 비우기

    if not stack:
        result.append(0)  # 스택이 비면 레이저를 수신한 탑이 없다는 뜻이므로 result에 "0" 데이터 추가

    stack.append([i, top[i]])  # 스택에 현재 신호탑 데이터 추가

for i in range(n):
        print(result[i], end=' ')


#2 MIN HEAP
class minHeap:
    def __init__(self):
        self.queue = [None]

    def swap(self, x, y):
        self.queue[x], self.queue[y] = self.queue[y], self.queue[x]

    def insert(self, n):
        self.queue.append(n)
        i = len(self.queue) - 1
        while i>1:
            parent = i // 2
            if self.queue[i] < self.queue[parent]:
                self.swap(i, parent)
                i = parent
            else: break
    def delete(self):
        if len(self.queue) > 1:
            self.swap(1, len(self.queue)-1)
            ans = self.queue.pop(len(self.queue)-1)
            self.minHeapify(1)
        else: ans = 0
        return ans
    def minHeapify(self, i):
        left = i*2
        right = i*2 + 1
        smallest = i

        if left <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]:
            smallest = left
        if right <= len(self.queue)-1 and self.queue[left] < self.queue[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.minHeapify(smallest)

if __name__ == '__main__':
    num = int(input())
    heap = minHeap()
    for i in range(num):
        x = int(input())
        if x == 0:
            print(heap.delete())
        else:
            heap.insert(x)