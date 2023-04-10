from collections import deque, defaultdict
N, L, R = map(int, input().split())
A = []

for _ in range(N):
    A.append(list(map(int, input().split())))
dx, dy = (1,-1,0,0), (0,0,1,-1)

iter = 0
while True:
    visited = [[0] * N for _ in range(N)]
    count = 0
    alliance = defaultdict(list)
    people = defaultdict(int)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                count +=1
                q = deque([(i,j,A[i][j])])
                visited[i][j] = 1
                alliance[count].append((i, j))
                people[count] += A[i][j]
                while q:
                    x, y, p = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0<=nx<N and 0<=ny<N:
                            if not visited[nx][ny]:
                                if L <= abs(A[nx][ny] - p) <=R:
                                    visited[nx][ny] = 1
                                    q.append((nx, ny, A[nx][ny]))
                                    alliance[count].append((nx, ny))
                                    people[count]+=A[nx][ny]
    if count == N*N:
        break
    else:
        iter += 1
        for team, member in alliance.items():
            total = people[team]
            for country in member:
                A[country[0]][country[1]] = total // len(member)

print(iter)

