N, M = map(int, input().split())

ice_frame = []
for _ in range(N):
    ice_frame.append(list(map(int, input().split())))


def dfs(i, j):
    if i <= -1 or i >= N or j <= -1 or j >= M:
        return 0
    if ice_frame[i][j] == 0:
        ice_frame[i][j] = True
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
        return 0

count = 0

for r in range(N):
    for c in range(M):
        if ice_frame[r][c] == 0:
            dfs(r, c)
            count += 1
print(count)
