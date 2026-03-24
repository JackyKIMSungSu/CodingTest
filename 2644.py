import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력

# ---------------------------
# 1. 입력 처리
# ---------------------------
n = int(input())                # 전체 사람 수 (정점 개수)
start, target = map(int, input().split())  # 촌수 계산 대상
m = int(input())                # 관계 수 (간선 개수)

# ---------------------------
# 2. 그래프 생성 (인접 리스트)
# ---------------------------
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    # 🔥 핵심: 부모-자식 관계지만 "양방향"으로 연결해야 함
    graph[x].append(y)
    graph[y].append(x)

# ---------------------------
# 3. BFS 함수 정의
# ---------------------------
def bfs(start, target):
    # 방문 여부 체크 배열
    visited = [False] * (n + 1)

    # 큐 생성 (현재 노드, 현재까지 촌수)
    queue = deque()
    queue.append((start, 0))  # 시작점은 촌수 0
    visited[start] = True     # 시작점 방문 처리

    # BFS 시작
    while queue:
        current, dist = queue.popleft()  # 현재 노드와 촌수

        # 🎯 목표 노드 도달 시 → 촌수 반환
        if current == target:
            return dist

        # 현재 노드와 연결된 사람들 탐색
        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True          # 큐에 넣을 때 방문 처리
                queue.append((nxt, dist + 1))  # 촌수 +1 해서 저장

    # ❌ 끝까지 못 찾으면 → 관계 없음
    return -1

# ---------------------------
# 4. 결과 출력
# ---------------------------
print(bfs(start, target))