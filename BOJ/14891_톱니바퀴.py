# 톱니바퀴 https://www.acmicpc.net/problem/14891 

import sys

def InputData():
  readl = sys.stdin.readline
  gear = [[int(x) for x in readl().strip()] for _ in range(4)]
  K = int(readl())
  move = [tuple(map(int, readl().split())) for _ in range(K)]

  return gear, K, move


def rotate(g : list, direction : int) -> list:
  """
  g :  gear list 
  direction : rotate direction, 1 : 시계방향, -1 반시계 방향
  return : rotated g
  """
  new_g = []
  if direction == 1:
    new_g = [g[-1]] + g[0:-1]
  elif direction == -1:
    new_g = g[1:] + [g[0]]
  return new_g

def moveable(base : list, compare : list, direction : int) -> bool:
  """
  base : 기준이 되는 톱니
  compare : 움직일 톱니
  direction : base 기준 compare 위치, 
              1 : 왼쪽, 
              -1 : 오른쪽
  """
  # 왼쪽과 비교
  if direction == 1:
    return base[6] != compare[2]
  # 오른쪽과 비교
  elif direction == -1:
    return base[2] != compare[6]
  return "error"

def iteration(gear : list, command : tuple) -> list:
  """
  gear : gear list
  command : (gear number, direction) direction, 1 : 시계방향, -1 반시계 방향
  """
  g, base_dir = command[0] -1, command[1]
  rotation = [(0,0)] * 4
  rotation[g] = (1, base_dir)

  # g 기준 왼쪽 오른쪽 분리 (인덱스로)
  left = [0,1,2,3][:g][::-1] # 역순으로 슬라이싱해서 루프 돌리기 편하게 함
  right = [0,1,2,3][g+1:]

  base = gear[g]
  dir = base_dir
  # base 기준 왼쪽
  for idx in left:
    if moveable(base, gear[idx], 1):
      base = gear[idx]
      dir = dir * -1
      rotation[idx] = (1, dir)
    else:
      break

  # base기준 오른쪽
  base = gear[g]
  dir = base_dir
  for idx in right:
    if moveable(base, gear[idx], -1):
      base = gear[idx]
      dir = dir * -1
      rotation[idx] = (1, dir)
    else:
      break

  new_gear = []
  for idx, g in enumerate(gear):
    if rotation[idx][0]:
      new_gear.append(rotate(g, rotation[idx][1]))
    else:
      new_gear.append(g)

  return new_gear

def sol(gear, K, move):
  for i in range(K):
    gear = iteration(gear, move[ i])

  return gear[0][0] + 2 * gear[1][0] + 4 * gear[2][0] + 8 * gear[3][0]


gear, K, move = InputData()
print(sol(gear, K, move))

