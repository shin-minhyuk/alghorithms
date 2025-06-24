import sys

input = sys.stdin.readline

N,K,B = list(map(int, input().split()))
A = [0] * N

for i in range(B):
  num = int(input())
  A[num-1] = 1

psum = [0] * N
psum[0] = A[0]

for i in range(1,N):
  psum[i] = psum[i-1] + A[i]

temp_psum = []
for i in range(N-K+1):
  if i == 0:
    sum = psum[i+K-1]
  else:
    sum = psum[i+K-1] - psum[i-1]
  temp_psum.append(sum)

print(min(temp_psum))
