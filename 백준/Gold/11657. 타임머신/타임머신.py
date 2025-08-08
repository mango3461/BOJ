# 벨만 포드 알고리즘 문제
# dist[v]=min(dist[v],dist[u]+w(u,v))
# 기존 v로 가는 길보다 u를 거쳐서 v에 도달하는 새로운 경로가 더 빠르면 v로 가는 길 갱신
# 새로운 지름길 발견과 같은 개념
import sys
INF = int(1e18)
input = sys.stdin.readline

n,m = map(int, input().split()) # n: 도시 개수, m: 버스 노선 개수
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellman_ford(start, n, edges):
    dist = [INF] * (n+1)    # length가 n+1인 무한대 배열
    dist[start] = 0

    for _ in range(n-1):  # 정점 수 - 1번 반복
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 음수 사이클 확인
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None  # 음수 사이클 존재

    return dist



start = 1  # 시작 도시 번호 
result = bellman_ford(start, n, edges)

if result is None:
    print(-1)
    sys.exit(0)
else:
    for i in range(2, n+1):
        if result[i] == INF:
            print(-1)
        else:
            print(result[i])