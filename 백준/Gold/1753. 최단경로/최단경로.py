import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = list(map(int, input().split()))
K = int(input())-1

adj = [[] for _ in range(V)]

for _ in range(E):
  u, v, w = list(map(int, input().split()))

  adj[u-1].append((v-1, w))

dist = [1e9] * V
pq = PriorityQueue()

dist[K] = 0
pq.put((0, K))

while pq.qsize() != 0:
  a, b = pq.get()

  if a != dist[b]:
    continue

  for c, d in adj[b]:
    if dist[c] > dist[b] + d:
      dist[c] = dist[b] + d
      pq.put((dist[c], c))

for i in range(V):
  if dist[i] == 1e9:
    print("INF")
  else:
    print(dist[i])
