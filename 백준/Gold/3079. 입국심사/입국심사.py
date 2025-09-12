import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

left = 1
right = min(times) * M
answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0
    for time in times:
        total += mid // time
        if total >= M:
            break

    if total >= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
