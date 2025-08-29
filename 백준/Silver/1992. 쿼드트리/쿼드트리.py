import sys

N = int(sys.stdin.readline())
video = [sys.stdin.readline().strip() for _ in range(N)]

def compress(x, y, size):
    first_pixel = video[x][y]
    is_same = True

    # 현재 영역이 모두 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != first_pixel:
                is_same = False
                break
        if not is_same:
            break

    # 모두 같은 색이라면 해당 색상 출력
    if is_same:
        print(first_pixel, end='')
        return

    # 다른 색이 섞여 있다면 4등분하여 재귀 호출
    half = size // 2
    print('(', end='')
    compress(x, y, half)             # 왼쪽 위
    compress(x, y + half, half)      # 오른쪽 위
    compress(x + half, y, half)      # 왼쪽 아래
    compress(x + half, y + half, half) # 오른쪽 아래
    print(')', end='')

# 함수 호출
compress(0, 0, N)
