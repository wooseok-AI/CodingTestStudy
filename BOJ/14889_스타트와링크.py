# 스타트와 링크 https://www.acmicpc.net/problem/14889

import sys

def InputData():
  readl = sys.stdin.readline
  N = int(readl())
  grid = [list(map(int, readl().split())) for _ in range(N)]

  return N, grid

def dfs(start, array, count):
  global N, grid, team_list, minScore

  if count == N//2:
    team_list.append(set(tuple(array)))
    return
  
  for x in range(start, N):
    dfs(x + 1, array + [x], count + 1)


N, grid = InputData()
team_list = []
min_score = float("inf")
dfs(0, [], 0)
all_player = set(tuple([x for x in range(N)]))

for start in team_list:
  score_start, score_link = 0, 0
  link = tuple(all_player - start)
  start = tuple(start)

  for i in range(N//2):
    for j in range(N//2):
      if i == j:
        continue
      score_start += grid[start[i]][start[j]]
      score_link += grid[link[i]][link[j]]
  
  min_score = min(min_score, abs(score_start - score_link))

print(min_score)

      
