import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[] for _ in range(N)]

for i in range(M):
  a, b = list(map(int, input().split()))

  adj[a-1].append(b-1)
  adj[b-1].append(a-1)

visit = [0] * N

def dfs(node):
  visit[node] = 1

  for neighbor in adj[node]:
    if not visit[neighbor]:
      dfs(neighbor)
  
dfs(0)
print(sum(visit) - 1)
