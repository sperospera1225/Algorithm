from collections import deque

# define 4 directions to move
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS sourcecode implementation
def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append((x,y,0))
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # if out of boundary
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if map[nx][ny] == 'W':
                continue

            if map[nx][ny] == 'L' and visited[nx][ny]==False:
                visited[nx][ny] == True
                # define each tomato number as the day it takes to be ripen
                # map[nx][ny]=map[x][y]+1
                queue.append((nx, ny, cnt+1))
    return cnt

if __name__=='__main__':
    n, m = map(int, input().split())
    # input 2 dimensional array
    map = list()
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        map.append(input().strip())
        #split하지않고 index로 접근하기
    result = 0
    for i in range(n):
        for j in range(m):
            print("aa")
            if bfs(i,j) >= result and visited[i][j]==False:
                print("bb")
                visited[i][j]=True
                result = bfs(i, j)
                print(bfs(i,j))
    print(result)