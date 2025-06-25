import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
parents = list(map(int, input().split()))

for i in range(1, N):
  parents[i] = parents[i] - 1

good = [0] * N
for _ in range(M):
  I, W = list(map(int, input().split()))
  good[I - 1] += W

total_good = [0] * N
for i in range(N):
  if parents[i] == -1:
    continue

  total_good[i] = total_good[parents[i]] + good[i]

print(*total_good)