import sys

input = sys.stdin.readline

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

results = []
total = 0
for p in permutations(A):
  for i in range(N-1):
    total += abs(p[i] - p[i+1])
  
  results.append(total)
  total = 0

print(max(results))