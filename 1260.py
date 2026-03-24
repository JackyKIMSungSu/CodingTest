import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프의 각 정점에 대해 오름차순으로 정렬
for i in range(1,  N + 1):
    graph[i].sort()

# DFS 구현
def dfs(v, visited):
    visited[v] = True
    print(v, end= ' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

# BFS 구현
def bfs(v):
    visited = [False] * (N + 1)
    queue = deque([v])
    visited[v] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# DFS와 BFS 실행
visited = [False] * (N + 1)
dfs(V, visited)
print()
bfs(V)
