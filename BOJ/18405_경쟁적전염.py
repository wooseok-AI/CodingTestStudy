from collections import deque

N, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())



dx, dy = (1,-1,0,0), (0,0,1,-1)
virus = []
for i in range(N):
    for j in range(N):
        if grid[i][j] !=0:
            virus.append((grid[i][j], 0, i, j))

q = deque(sorted(virus))

while q:
    k, s, x, y = q.popleft()
    if s == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if grid[nx][ny] == 0:
                grid[nx][ny] = k
                q.append((k, s+1, nx, ny))

print(grid[X-1][Y-1])
