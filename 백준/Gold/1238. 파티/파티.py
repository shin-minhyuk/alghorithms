import sys
from queue import PriorityQueue
input = sys.stdin.readline

# N명, M개의 단방향 도로, X번 마을
N, M, X = list(map(int, input().split()))
X -= 1

adj = [[] for _ in range(N)]
reverse_adj = [[] for _ in range(N)]

for _ in range(M):
  u, v, w = list(map(int, input().split()))

  adj[u-1].append((v-1, w))
  reverse_adj[v-1].append((u-1, w))

dist = [1e9] * N
pq = PriorityQueue()

dist[X] = 0
pq.put((0, X))

while pq.qsize() != 0:
  d, u = pq.get()

  if d != dist[u]:
    continue

  for v, w in adj[u]:
    if dist[v] > dist[u] + w:
      dist[v] = dist[u] + w
      pq.put((dist[v], v))

reverse_dist = [1e9] * N
pq = PriorityQueue()

reverse_dist[X] = 0
pq.put((0, X))

while pq.qsize() != 0:
  d, u = pq.get()

  if d != reverse_dist[u]:
    continue

  for v, w in reverse_adj[u]:
    if reverse_dist[v] > reverse_dist[u] + w:
      reverse_dist[v] = reverse_dist[u] + w
      pq.put((reverse_dist[v], v))

max_dist = 0
for i in range(N):
  if max_dist < dist[i] + reverse_dist[i]:
    max_dist = dist[i] + reverse_dist[i]

print(max_dist)

