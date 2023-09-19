# 경사로 https://www.acmicpc.net/problem/14890
import sys

def InputData():
  readl = sys.stdin.readline
  N, L = map(int, readl().split())
  grid = [list(map(int, readl().split())) for _ in range(N)]
  return N, L, grid

N, L, grid = InputData()

slope_data = [[0] * N for _ in range(N)]

def check_if(N, L, line):
  prev = 0
  count = 0
  slope = [0] * N
  available = True
  for i in range(N):
    current = line[i]
    if not prev or prev == current:
      prev = current
      count += 1
      continue
    # 더 높은 블럭이 1차이 나야함
    if abs(prev - current) == 1:
      # 1 높아질 때
      if prev + 1 == current:
        if count >= L:
          if slope[i-L:i] != [0] * L:
            return 0
          slope[i-L:i] = [1] * L
        else:
          return 0
      # 1 낮아질 때
      elif prev - 1 == current:
        if i + L <= N:
          if line[i: i+L] == [current] * L:
            slope[i: i+L] = [1] * L
          else:
            return 0
        else:
          return 0
      prev = current
      count = 1
    # 차이가 1보다 크면 못건넘
    else:
      return 0
  return 1

def sol():
  result = 0
  for i in range(N):
    result += check_if(N, L, grid[i])
  
  for j in range(N):
    line = [grid[x][j] for x in range(N)]
    result += check_if(N, L, line)

  print(result)

sol()