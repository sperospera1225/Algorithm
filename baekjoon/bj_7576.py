from collections import deque

# define 4 directions to move
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS sourcecode implementation
def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # if out of boundary
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # if unripen tomato exists
            if tomato[nx][ny] == 0:
                # define each tomato number as the day it takes to be ripen
                tomato[nx][ny]=tomato[x][y]+1
                queue.append((nx, ny))
    if max(map(max, tomato)) == 1:
        return 0
    # at least one unripen tomato exist in tomato array
    elif any(0 in l for l in tomato):
        return -1
    else:
        return max(map(max, tomato)) - 1


if __name__=='__main__':
    m, n = map(int, input().split())
    # input 2 dimensional array
    tomato = list()
    for i in range(n):
        tomato.append(list(map(int, input().split())))
    print(bfs())
