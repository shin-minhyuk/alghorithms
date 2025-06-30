import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 인접 리스트 생성
adj = [[] for _ in range(N)]

# 친구 관계 입력
for _ in range(M):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

# 최소 케빈 베이컨 수를 찾기 위해 변수 준비
min_total = int(1e9)
answer = -1

# 모든 사람을 시작점으로 BFS 실행
for i in range(N):
    visit = [False] * N    # 방문 여부
    dist = [-1] * N        # 각 사람까지의 최단 거리 저장

    queue = deque([i])     # 시작점 큐에 넣기
    visit[i] = True
    dist[i] = 0            # 자기 자신까지 거리는 0

    while queue:
        u = queue.popleft()   # 현재 사람 u

        for v in adj[u]:      # u의 친구들 탐색
            if not visit[v]:  # 아직 방문 안 했으면
                queue.append(v)             # 큐에 추가
                visit[v] = True             # 방문 처리
                dist[v] = dist[u] + 1       # 거리 = 현재 거리 + 1

    total = sum(dist)    # i번 사람의 케빈 베이컨 수 = 모든 거리 합

    # 최소 케빈 베이컨 수를 가진 사람 찾기
    if total < min_total:
        min_total = total
        answer = i

# 문제는 사람 번호가 1번부터 시작하니까 +1 출력
print(answer + 1)