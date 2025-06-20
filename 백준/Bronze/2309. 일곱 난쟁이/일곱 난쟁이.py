import sys

input = sys.stdin.readline

from itertools import combinations

pocket = []
result = []
for i in range(9):
  N = int(input())
  pocket.append(N)


new = list(combinations(pocket, 7))

for n in new:
  if sum(n) == 100:
    result.extend(list(n))
    break

result.sort()

for i in result:
  print(i)