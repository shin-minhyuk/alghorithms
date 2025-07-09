import sys
input = sys.stdin.readline

N = int(input())

X = [0] * (N + 1)
X[1] = 0

for i in range(2, N + 1):
	X[i] = 1 + X[i - 1]

	if i % 3 == 0:
		X[i] = min(X[i], 1 + X[i // 3])
	if i % 2 == 0:
		X[i] = min(X[i], 1 + X[i // 2])

print(X[N])
