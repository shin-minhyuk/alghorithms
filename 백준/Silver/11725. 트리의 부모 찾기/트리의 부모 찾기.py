import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
M = N - 1

adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visit = [False] * N
parent = [-1] * N

def dfs(node):
    visit[node] = True
    for child in adj[node]:
        if not visit[child]:
            parent[child] = node
            dfs(child)

dfs(0)

for i in range(1, N):
    print(parent[i] + 1)