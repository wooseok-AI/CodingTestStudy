from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
grid = []
R, B = (0, 0), (0, 0)
for r in range(N):
  row = list(input())
  grid.append(row)
  if 0 < r < N-1:
    for c in range(M):
      if row[c] == "R":
        rx, ry = r, c
      elif row[c] == "B":
        bx, by = r, c      
  else:
    continue
dx, dy = (1,-1, 0, 0), (0, 0, 1, -1)
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

q = deque([(rx, ry, bx, by, 1)])
visited[rx][ry][bx][by] = 1

def move(x, y, dx, dy):
  count = 0 
  while grid[x +dx][y + dy] != "#" and grid[x][y] != "O":
    x = x + dx
    y = y + dy
    count += 1
  return x, y, count


def bfs():
  
  while q:
    rx, ry, bx, by, depth = q.popleft()
    if depth > 10:
      break
    
    for d in range(4):
      n_rx, n_ry, r_count = move(rx, ry, dx[d], dy[d])
      n_bx, n_by, b_count = move(bx, by, dx[d], dy[d])

      if grid[n_bx][n_by] == "O":
        continue
      if grid[n_rx][n_ry] == "O":
        print(depth)
        return
      if n_rx == n_bx and n_ry == n_by:
        if r_count > b_count:
          n_rx -= dx[d]
          n_ry -= dy[d]
        else:
          n_bx -= dx[d]
          n_by -= dy[d]

      if not visited[n_rx][n_ry][n_bx][n_by]:
        visited[n_rx][n_ry][n_bx][n_by] = 1
        q.append((n_rx, n_ry, n_bx, n_by, depth + 1))
  print(-1)

bfs()


