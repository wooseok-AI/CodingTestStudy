# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:29:01 2020

@author: arm45
"""


def bfs(startpoint, country, visited):
    
    queue = []
    queue.append(startpoint)
    visited[startpoint] = 1
    cnt = 0
    while queue:
       current = queue.pop(0)
       for i in country[current]:
           if visited[i] == 0:
               queue.append(i)
               visited[i] = 1
               cnt += 1
               
    return cnt

def dfs(startpoint, country, visited):
    stack = []
    stack.append(startpoint)
    visited[startpoint] = 1
    cnt = 0
    
    while stack:
        current = stack.pop(-1)
        for i in country[current]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                cnt +=1
                
    return cnt    
test_case = int(input())

while(test_case > 0):
    
    N, M = list(map(int, input().split()))
    
    country = [[] for _ in range(N)]
    visited = [0] * N
    
    for _ in range(M):
        a, b = list(map(int, input().split()))
        country[a-1].append(b-1)
        country[b-1].append(a-1)
        
    for i in range(N):
        if visited[i] == 0:
            ans = dfs(i, country, visited)
            break
    
    test_case -=1
    print(ans)