import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


for k in range(N): # 거쳐가는 노드
    for i in range(N): # 시작 노드
        for j in range(N): # 도착 노드
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1 # 경로 존재 표시

for row in graph:
    print(*row)
