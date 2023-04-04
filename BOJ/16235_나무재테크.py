from collections import deque

# N: 맵의 크기, M: 나무의 수, K: 기준 년
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
T = [[deque() for _ in range(N)] for _ in range(N)]
nutrition = [[5] * N  for _ in range(N)]
dr, dc = (-1,-1,-1,0,0,1,1,1), (-1,0,1,-1,1,-1,0,1)

for _ in range(M):
    r, c, age = map(int, input().split())
    T[r-1][c-1].appendleft(age)


def spring_summer():
    for i in range(N):
        for j in range(N):
            for k in range(len(T[i][j])):
                if T[i][j][k] <= nutrition[i][j]:
                    nutrition[i][j] -= T[i][j][k]
                    T[i][j][k] += 1
                else:
                    for _ in range(k, len(T[i][j])):
                        nutrition[i][j] += T[i][j].pop() // 2
                    break


def fall_winter():
    for x in range(N):
        for y in range(N):
            for z in range(len(T[x][y])):
                if T[x][y][z] % 5 == 0:
                    for idx in range(8):
                        nr = x + dr[idx]
                        nc = y + dc[idx]
                        if 0 <= nr < N and 0 <= nc < N:
                            T[nr][nc].appendleft(1)
            nutrition[x][y] += A[x][y]

for _ in range(K):
    spring_summer()
    fall_winter()

count = 0
for i in range(N):
    for j in range(N):
        count += len(T[i][j])

print(count)




