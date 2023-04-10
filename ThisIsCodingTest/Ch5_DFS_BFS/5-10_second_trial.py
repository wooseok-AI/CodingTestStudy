from collections import deque

N, M = map(int, input().split())
ice = [list(map(int, input())) for _ in range(N)]


def num_ice():
    rx, ry = (1, -1, 0, 0), (0, 0, 1, -1)
    num = 0
    for i in range(N):
        for j in range(M):
            ice_que = deque()
            if ice[i][j] == 0:
                ice_que.append((i, j))
                ice[i][j] = 1
                print("\nnew_queue : ", ice_que)
                while ice_que:
                    position = ice_que.popleft()
                    for d in range(4):
                        nx = position[0] + rx[d]
                        ny = position[1] + ry[d]
                        if 0 <= nx < N and 0 <= ny < M:
                            if ice[nx][ny] == 0:
                                ice[nx][ny] = 1
                                ice_que.append((nx, ny))
                                print(ice_que)
                num += 1

    return num

print(num_ice())

