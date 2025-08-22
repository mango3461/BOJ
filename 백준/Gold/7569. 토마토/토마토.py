import sys
from collections import deque

input = sys.stdin.readline

# M: 가로, N: 세로, H: 높이
M, N, H = map(int, input().split())

# 상자 상태 입력
box = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    box.append(layer)

# 방문 체크
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

# 6방향 이동 (위, 아래, 상, 하, 좌, 우)
directions = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

# BFS 함수
def bfs():
    q = deque()
    
    # 시작점: 익은 토마토 위치 모두 큐에 넣기
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    q.append((z, y, x))
                    visited[z][y][x] = True
    
    while q:
        z, y, x = q.popleft()
        for dz, dy, dx in directions:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if not visited[nz][ny][nx] and box[nz][ny][nx] == 0:
                    visited[nz][ny][nx] = True
                    box[nz][ny][nx] = box[z][y][x] + 1  # 날짜 계산
                    q.append((nz, ny, nx))

# BFS 실행
bfs()

# 결과 계산
result = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                print(-1)
                sys.exit(0)
            result = max(result, box[z][y][x])

print(result - 1)  # 익은 토마토 1부터 시작했으므로 1 빼기
