from collections import deque

N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]

def find_min():
    min_move = 9887654321
    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    move = deque()
    move.append((0, 0))
    count = 0
    while move:
        position = move.popleft()
        x, y = position[0], position[1]
        if x == N-1 and y == M-1:
            min_move = min(min_move, count)
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if A[nx][ny] == 0:
                    continue
                if A[nx][ny] == 1:
                    A[nx][ny] = A[x][y] + 1
                    move.append((nx, ny))
    return A[N-1][M-1]

print(find_min())
print(A)
