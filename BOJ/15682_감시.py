#감시 https://www.acmicpc.net/problem/15683

# 감시 https://www.acmicpc.net/problem/15683
import sys 
from copy import deepcopy 
def InputData():
  readl = sys.stdin.readline
  N, M = map(int, readl().split())
  grid = []
  cctv = []
  wall = 0
  for n in range(N):
    row = list(map(int, readl().split()))
    grid.append(row)
    for m in range(M):
      if 1<= row[m] <=5:
        cctv.append((n,m,row[m]))
      elif row[m] == 6:
        wall += 1
  
  return N, M, grid, cctv, wall


def find_combination(cctv : list, camera_direction : dict) -> list:
  """
  cctv : cctv list, (r, c, num)
  camera_direction : dict[key] = [(dx, dy) ... ]
  """
  c_num = len(cctv)
  combination = [] # [(카메라 r, 카메라 c, 카메라 번호, 방향 인덱스)]

  def dfs(c_index : int, array : list):

    if c_index == c_num:
      combination.append(array)
      return
    
    r, c, num = cctv[c_index]

    for d in camera_direction[num]:
      if type(d) == int:
        d = [d]
      dfs(c_index + 1, array + [(r,c,d)])
  
  dfs(0, [])
  return combination



def blind_sight(N : int , M : int, grid : list, camera : tuple, wall : int) -> int:
  """
  grid : 현재 지도
  camera : [(r,c, 방향리스트), ...]
  wall : number of walls, 사각지대 개수 확인
  """
  
  #사각지대 :  N * M - wall - 감시지역 - camera 개수
  dx, dy = (1,0,-1,0), (0,1,0,-1)
  sight_count = 0

  for cam in camera:
    # print(cam)
    r, c, direction = cam
    
    for d in direction:
      cr, cc = r, c
      while True:
        nr, nc = cr + dx[d], cc + dy[d]
        if 0<=nr<N and 0<=nc<M:
          if grid[nr][nc]!= 6:
            if grid[nr][nc] == 0:
              grid[nr][nc] = "#"
              sight_count += 1
          else:
            break
          cr, cc = nr, nc
        else:
          break

  return N * M - wall - len(camera) - sight_count, grid

def sol():
  N, M, grid, cctv, wall = InputData()
  
  camera_direction = {
    1 : [(0),(1),(2),(3)],
    2 : [(0, 2), (1, 3)],
    3 : [(0, 1), (1, 2), (2, 3), (3, 0)],
    4 : [(0,1,2), (1,2,3), (2,3,0), (3,0,1)],
    5 : [(0,1,2,3)]
  }

  combination = find_combination(cctv, camera_direction)

  min_blackspot = N*M + 1
  # 조합별로 grid 만들어서 점수 체크
  for case in combination:
    sample_grid = deepcopy(grid)
    case_blindsight, result = blind_sight(N, M, sample_grid, case, wall)
    # print(result)
    min_blackspot = min(case_blindsight, min_blackspot)

  return min_blackspot

print(sol())