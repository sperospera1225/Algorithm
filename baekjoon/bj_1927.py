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