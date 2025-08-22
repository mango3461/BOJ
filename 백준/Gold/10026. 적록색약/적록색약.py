import sys
from collections import deque
input = sys.stdin.readline

# 세로 N
N = int(input())
# 색상 정보 입력
box = [list(input().strip()) for _ in range(N)]
# 가로 M
M = len(box[0])

# 상하좌우
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# 일반인 BFS
def bfs(y, x, color, visited):
    q = deque([(y, x)])
    visited[y][x] = True
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and box[ny][nx] == color:
                    visited[ny][nx] = True
                    q.append((ny, nx))

# 적록색약 BFS
def bfs_colorblind(y, x, color, visited):
    q = deque([(y, x)])
    visited[y][x] = True
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                next_color = box[ny][nx]
                if (color in 'RG' and next_color in 'RG') or (color == next_color):
                    visited[ny][nx] = True
                    q.append((ny, nx))

# 일반인 영역 개수 계산
visited_normal = [[False]*M for _ in range(N)]
normal_count = 0
for y in range(N):
    for x in range(M):
        if not visited_normal[y][x]:
            bfs(y, x, box[y][x], visited_normal)
            normal_count += 1

# 적록색약 영역 개수 계산
visited_colorblind = [[False]*M for _ in range(N)]
colorblind_count = 0
for y in range(N):
    for x in range(M):
        if not visited_colorblind[y][x]:
            bfs_colorblind(y, x, box[y][x], visited_colorblind)
            colorblind_count += 1

print(normal_count, colorblind_count)
