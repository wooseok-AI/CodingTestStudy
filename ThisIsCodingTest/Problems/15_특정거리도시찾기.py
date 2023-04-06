N, M, K, X = map(int, input().split())
X= X-1
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1


min_distance_graph = [[-1] * N for _ in range(N)]

def path_find(origin, start_node, destination, distance, visited):

    if start_node == destination:

        if min_distance_graph[origin][destination] == -1:
            min_distance_graph[origin][destination] = distance
        else:
            min_distance_graph[origin][destination] = min(min_distance_graph[origin][destination], distance)
        return

    for idx in range(N):
        if graph[start_node][idx] != 0:
            if visited[idx] == 1:
                continue
            visited[start_node] = 1
            path_find(origin, idx, destination, distance + 1, visited)

find = False
for i in range(N):
    start_node = X
    destination = i
    min_dis = -1
    visited = [0] * N
    path_find(start_node, start_node, destination, 0, visited)
    dis = min_distance_graph[start_node][destination]
    if dis == K:
        find = True
        print(i+1)
if not find:
    print(-1)
