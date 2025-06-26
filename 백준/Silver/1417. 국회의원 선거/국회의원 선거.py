import sys

input = sys.stdin.readline

N = int(input())

cardidate = [0] * N
for i in range(N):
  cardidate[i] = int(input())

count = 0

if N == 1:
  print(0)
else:
  while True:
    max_votes = max(cardidate[1:])

    if cardidate[0] > max_votes:
      break

    index = cardidate[1:].index(max_votes) + 1
    cardidate[index] -= 1
    cardidate[0] += 1
    count += 1

if N != 1:
  print(count)
