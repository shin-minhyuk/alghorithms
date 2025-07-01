import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))

adj = [[] for _ in range(N)]

for _ in range(M):
  a, b = list(map(int, input().split()))

  adj[a-1].append(b-1)
  adj[b-1].append(a-1)

min_kevin_bacon = 1e9
min_person = -1

for i in range(N):
  visit = [False] * N
  dist = [-1] * N

  queue = deque([i])
  visit[i] = True
  dist[i] = 0

  while len(queue) != 0:
    u = queue.popleft()

    for v in adj[u]:
      if not visit[v]:
        queue.append(v)
        visit[v] = True
        dist[v] = dist[u] + 1
  
  kevin = sum(dist)

  if min_kevin_bacon > kevin:
    min_kevin_bacon = kevin
    min_person = i + 1

print(min_person)