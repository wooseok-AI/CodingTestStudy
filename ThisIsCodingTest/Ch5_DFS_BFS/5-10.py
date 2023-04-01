# 실전문제 3. 음료수 얼려먹기
from collections import deque


def solution(N: int, M: int, graph: list, visited: list):
    count = 0
    for i in range(N):
        for j in range(M):
            queue = deque()
            if not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j))
                while queue:
                    node = queue.popleft()
                    for n in graph[node]:
                        if not visited[n[0]][n[1]]:
                            queue.append(n)
                            visited[n[0]][n[1]] = True
                count += 1

    return count


if __name__ == "__main__":
    # ice_frame = [
    #     [0, 0, 1, 1, 0],
    #     [0, 0, 0, 1, 1],
    #     [1, 1, 1, 1, 1],
    #     [0, 0, 0, 0, 0]
    # ]
    N, M = list(map(int, input().split()))
    ice_frame = []
    for i in range(N):
        row = list(map(int, input().split()))
        ice_frame.append(row)

    N = len(ice_frame)
    M = len(ice_frame[0])
    INF = 999999

    visited = [[0] * M for _ in range(N)]
    graph = dict()
    # 그래프 생성
    log = []
    for i in range(N):
        for j in range(M):
            if ice_frame[i][j] == 0:
                graph[(i, j)] = []
                # 상
                if i - 1 >= 0:
                    if ice_frame[i - 1][j] == 0:
                        graph[(i, j)].append((i - 1, j))
                # 하
                if i + 1 < N:
                    if ice_frame[i + 1][j] == 0:
                        graph[(i, j)].append((i + 1, j))
                # 좌
                if j - 1 >= 0:
                    if ice_frame[i][j - 1] == 0:
                        graph[(i, j)].append((i, j - 1))
                # 우
                if j + 1 < M:
                    if ice_frame[i][j + 1] == 0:
                        graph[(i, j)].append((i, j + 1))

            else:
                log.append((i, j))
                visited[i][j] = INF
                continue

    ice_count = solution(N, M, graph, visited)
    print(ice_count)
