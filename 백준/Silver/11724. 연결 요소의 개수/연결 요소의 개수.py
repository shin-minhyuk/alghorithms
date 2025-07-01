import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))

adj = [[] for _ in range(N+1)]

for _ in range(M):
  u, v = list(map(int, input().split()))

  adj[u].append(v)
  adj[v].append(u)

visit = [False] * (N+1)
count = 0

for i in range(1, N+1):
  # 만약 i가 방문한 위치라면 카운트 다음으로 넘어가기.
  if visit[i]:
    continue

  count += 1
  queue = deque([i])

  # 그게 아니면 카운트를 1을 올리고,
  # 거기 관련된 모든곳을 True 처리로 해야함.
  # 큐에 인덱스를 넣고, 그 인덱스를 지우면서 그 인덱스에 들어있는 
  # 인접 리스트를 전부 큐에 넣고 큐를 지우면서 방문을 추가하는 형태로 작업
  while len(queue) != 0:
    u = queue.popleft()

    for v in adj[u]:
      if not visit[v]:
        queue.append(v)
        visit[v] = True
  
print(count)






