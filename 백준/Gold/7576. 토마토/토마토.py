import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

# BFS 준비
queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:  # 익은 토마토
            queue.append((i, j))

# 상하좌우 이동 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 실행
while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1  # 날짜 증가
            queue.append((nx, ny))

# 결과 계산
result = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:  # 익지 못한 토마토 존재
            print(-1)
            sys.exit()
        result = max(result, box[i][j])

# 첫날이 1로 시작했으니 1 빼기
print(result - 1)
