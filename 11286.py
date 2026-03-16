import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x == 0:
        print(heappop(heap)[1] if heap else 0)
        # 스택이 비어 있지 않으면 (if heap) 절댓값이 가장 작은 수를 꺼내 출력합니다.
        # 스택이 비어있으면 (else) 0을 출력합니다.
    else:
        heappush(heap, (abs(x), x))
        # 0 이외의 수가 들어오면 tuple(x의 절댓값, x)을 heap에 넣습니다.
        # 최소힙이기 때문에 절댓값이 가장 작은 원소가 0번에 위치하며
        # 가장 작은 절댓값이 여러개인 경우 추가적으로 두번째 원소까지 비교합니다.