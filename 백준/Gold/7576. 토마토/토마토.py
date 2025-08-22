import sys
from collections import deque

input = sys.stdin.readline

# M: 가로, N: 세로
M, N = map(int, input().split())

# 상자 상태 입력
box = [list(map(int, input().split())) for _ in range(N)]

# 방문 체크
visited = [[False]*M for _ in range(N)]

# 4방향 이동 (상, 하, 좌, 우)
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# BFS 함수
def bfs():
    q = deque()
    
    # 시작점: 익은 토마토 위치 모두 큐에 넣기
    for y in range(N):
        for x in range(M):
            if box[y][x] == 1:
                q.append((y, x))
                visited[y][x] = True
    
    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and box[ny][nx] == 0:
                    visited[ny][nx] = True
                    box[ny][nx] = box[y][x] + 1  # 날짜 계산
                    q.append((ny, nx))

# BFS 실행
bfs()

# 결과 계산
result = 0
for y in range(N):
    for x in range(M):
        if box[y][x] == 0:
            print(-1)
            sys.exit(0)
        result = max(result, box[y][x])

print(result - 1)  # 익은 토마토 1부터 시작했으므로 1 빼기
