import sys
input = sys.stdin.readline

def draw_star(x, y, size):
    if size == 1:
        board[x][y] = '*'
        return

    sub_size = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 가운데는 비움
                continue
            draw_star(x + i * sub_size, y + j * sub_size, sub_size)

# 입력
N = int(input())
board = [[' ' for _ in range(N)] for _ in range(N)]

# 별 그리기
draw_star(0, 0, N)

# 출력
for row in board:
    print(''.join(row))
