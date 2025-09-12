import sys
input = sys.stdin.readline

N, M = map(int, input().split())
colors = [int(input()) for _ in range(M)]

left = 1
right = max(colors)
answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0
    for c in colors:
        total += (c + mid - 1) // mid
        if total > N:
            break
    if total > N:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
