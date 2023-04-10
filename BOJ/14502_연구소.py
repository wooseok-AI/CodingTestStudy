<<<<<<< HEAD
N, M = map(int, input().split())

lab = []
for _ in range(N):
    lab.append(list(map(int, input().split())))

wall =[]
visited = [[0] * M for _ in range(N)]

def dfs(cnt, wall_list):
    if cnt == 3:
        wall.add(wall_list)
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(cnt+1, wall_list + [(i,j)])
                visited[i][j] = 0

dfs(0,[])
print(wall)
print(len(wall))
=======
from collections import deque
from copy import deepcopy
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def find_wall(N, M, grid):
    wall_list = set()
    visited = [[0] * M for _ in range(N)]
    def dfs(N, M, grid, visited, count, array):

        if count == 3:
            wall_list.add(tuple(sorted(array)))
            return

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    if not visited[i][j]:
                        visited[i][j] = 1
                        dfs(N, M, grid, visited, count+1, array + [(i,j)])
                        visited[i][j] = 0

    dfs(N, M, grid, visited, 0, [])

    return wall_list

def virus(G, N, M, wall):
    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    for w in wall:
        G[w[0]][w[1]] = 1

    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if G[i][j] == 2 and not visited[i][j]:
                visited[i][j] = 1
                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0<=nx<N and 0<=ny<M:
                            if G[nx][ny] == 0:
                                if not visited[nx][ny]:
                                    visited[nx][ny] = 1
                                    G[nx][ny] = 2
                                    q.append((nx, ny))

    return G

def count_safe(N, M, G):

    count = 0
    for i in range(N):
        for j in range(M):
            if G[i][j] == 0:
                count+=1

    return count


test = ((0,1), (1,0), (3,5))
test2 = ((0,3), (1,3),(3,3))

wall_list = find_wall(N, M,grid)
max_count = -1
for wall in wall_list:
    G = deepcopy(grid)
    G = virus(G, N, M, wall)
    count = count_safe(N,M,G)
    if count > max_count:
        max_count = count
print(max_count)

# G = deepcopy(grid)
# G = virus(G, N, M, wall)
# print(G)
# count = count_safe(N,M,G)
# print(count)
>>>>>>> origin/master
