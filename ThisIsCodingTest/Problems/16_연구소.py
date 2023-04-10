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
