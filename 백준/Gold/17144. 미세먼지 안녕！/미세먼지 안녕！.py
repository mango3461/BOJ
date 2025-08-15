import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())

room = []
samsung = []

for i in range(r):
    row = list(map(int, input().split()))
    room.append(row)
    if row[0] == -1:
        samsung.append(i)
        
def spread():
    temp = [[0]*c for _ in range(r)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                amount = room[x][y] // 5
                spread_count = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx <r and 0 <= ny < c and room[nx][ny] != -1:
                        temp[nx][ny] += amount
                        spread_count += 1
                temp[x][y] += room[x][y] - amount*spread_count
    # 공기청정기
    for s in samsung:
        temp[s][0] = -1
    return temp

def clean():
    up, down = samsung[0], samsung[1]

    # 1. 위쪽 공기청정기 (반시계 방향)
    for i in range(up-1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(c-1):
        room[0][i] = room[0][i+1]
    for i in range(up):
        room[i][c-1] = room[i+1][c-1]
    for i in range(c-1, 1, -1):
        room[up][i] = room[up][i-1]
    room[up][1] = 0

    # 2. 아래쪽 공기청정기 (시계 방향)
    for i in range(down+1, r-1):
        room[i][0] = room[i+1][0]
    for i in range(c-1):
        room[r-1][i] = room[r-1][i+1]
    for i in range(r-1, down, -1):
        room[i][c-1] = room[i-1][c-1]
    for i in range(c-1, 1, -1):
        room[down][i] = room[down][i-1]
    room[down][1] = 0

for _ in range(t):
    room = spread()  # 미세먼지 확산
    clean()          # 공기청정기 작동

dust_sum = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            dust_sum += room[i][j]
print(dust_sum)
