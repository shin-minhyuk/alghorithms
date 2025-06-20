import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

pos1 = 0
pos2 = 0

while pos1 < N and pos2 < M:
  candidate1 = A[pos1]
  candidate2 = B[pos2]

  if candidate1 < candidate2:
    C.append(candidate1)
    pos1 += 1
  else:
    C.append(candidate2)
    pos2 += 1

if pos1 != N:
  C.extend(A[pos1:len(A)])
if pos2 != M:
  C.extend(B[pos2:len(B)])

for i in range(N + M):
  print(C[i], end=" ")
  


