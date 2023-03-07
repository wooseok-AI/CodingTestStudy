def dijkstra(graph, start):
    
    visited = [0] * len(graph)
    distance = [1000] * len(graph)
    current = start
    
    visited[current] = 1
    
    distance[current] = 0
    for vertex in graph[current]:
        distance[vertex] = 1
        
    while 0 in visited:        
        
        for vertex in graph[current]:
            if visited[vertex] == 0:
                distance[vertex] = min(distance[vertex], 
                                       distance[current]+1)
        
        minimum = 100
        
        for vertex, x in enumerate(distance):
            if x < minimum and visited[vertex] == 0:
                    minimum = x
                    current = vertex
                    
        visited[current] = 1
     
    return sum(distance), distance

N, M = list(map(int, input().split()))

adj_matrix = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    adj_matrix[a-1].append(b-1)
    adj_matrix[b-1].append(a-1)
    
result = []

for user in range(N):
    CB, _ = dijkstra(adj_matrix, user)
    result.append(CB)
    
print(result.index(min(result))+1)