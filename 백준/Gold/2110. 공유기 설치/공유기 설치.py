import sys
input = sys.stdin.readline

n, c = map(int, input().split())
pos = [int(input()) for _ in range(n)]
pos.sort()

def can_install(dist):
    count = 1
    last_pos = pos[0]
    for i in range(1, n):
        if pos[i] - last_pos >= dist:
            count += 1
            last_pos = pos[i]
    return count >= c

low, high = 1, pos[-1] - pos[0]
answer = 0
while low <= high:
    mid = (low + high) // 2
    if can_install(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
