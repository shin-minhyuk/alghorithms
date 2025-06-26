import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

# 상근이는 0번으로 가정
adj = [[] for _ in range(N)]
for i in range(M):
  a, b = list(map(int, input().split()))
  adj[a-1].append(b-1)
  adj[b-1].append(a-1)

friend = [0] * N
for i in adj[0]:
  friend[i] = 1

friend2 = [0] * N
for i in range(N):
  if friend[i] == 0:
    continue
  for j in adj[i]:
    if j != 0 and friend[j] == 0:
      friend2[j] = 1

print(sum(friend) + sum(friend2))
