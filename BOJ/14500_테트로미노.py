# 테트로미노 https://www.acmicpc.net/problem/14500
import sys
from collections import deque
from copy import deepcopy

def InputData():
  readl = sys.stdin.readline
  N, M = map(int, input().split())
  grid = [list(map(int, input().split())) for _ in range(N)]

  return N, M , grid


N, M, grid = InputData()
dx, dy = (1, 0, 0), (0, 1, -1)
count = 1
visited =[[0] * M for _ in range(N)]
maxScore = -1

def dfs(x, y, score, count):
  global N, M, dx, dy, maxScore

  if count == 4:
    maxScore = max(maxScore, score)
    return
  
  
  for d in range(3):
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < N and 0<= ny < M:
      if not visited[nx][ny]:
        visited[nx][ny] = 1
        dfs(nx, ny, score + grid[nx][ny], count + 1)
        visited[nx][ny] = 0

def solution():
  global N, M, maxScore
  di, dj = (1,-1,0,0), (0,0,1,-1)

  for i in range(N):
    for j in range(M):
      visited[i][j] = 1
      dfs(i, j, grid[i][j], 1)
      visited[i][j] = 0

      candidate = []
      for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0<=ni<N and 0<=nj<M:
          candidate.append(grid[ni][nj])
      
      maxScore = max(maxScore, grid[i][j] + sum(sorted(candidate, reverse=True)[:3]))

  return maxScore

print(solution())

