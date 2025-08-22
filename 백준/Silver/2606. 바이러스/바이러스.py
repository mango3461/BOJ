import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    count = 0
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1
    return count

print(bfs(1))