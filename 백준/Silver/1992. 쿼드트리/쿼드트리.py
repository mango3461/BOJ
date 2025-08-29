import sys

N = int(input())
image = [input().strip() for _ in range(N)]

def quad_tree(n, y, x):
    initial = image[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if image[i][j] != initial:
                half = n // 2
                return "(" + \
                    quad_tree(half, y, x) + \
                    quad_tree(half, y, x + half) + \
                    quad_tree(half, y + half, x) + \
                    quad_tree(half, y + half, x + half) + ")"
    return initial

print(quad_tree(N, 0, 0))

