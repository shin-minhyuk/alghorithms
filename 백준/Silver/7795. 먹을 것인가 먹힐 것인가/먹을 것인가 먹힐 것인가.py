import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N, M = list(map(int, input().split()))
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  A = sorted(A)
  B = sorted(B)

  idxA = 0
  idxB = 0
  count = 0

  while idxA < N:
    if idxB == M:
      count += idxB
      idxA += 1
    else:
      if A[idxA] > B[idxB]:
        idxB += 1
      else:
        count += idxB
        idxA += 1
  

  print(count)