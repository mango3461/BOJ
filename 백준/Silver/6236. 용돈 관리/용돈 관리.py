import sys
input = sys.stdin.readline

N, M = map(int, input().split())
expenses = [int(input()) for _ in range(N)]

# 주어진 K로 M번 이하로 인출 가능한지 확인
def can_withdraw(K):
    count = 1      # 첫 번째 인출
    total = 0
    for expense in expenses:
        if total + expense > K:  # 현재 잔액으로 부족하면 인출
            count += 1
            total = expense
        else:
            total += expense
    return count <= M

# 이진 탐색으로 최소 K 찾기
left = max(expenses)   # 하루 최대 지출 이상이어야 함
right = sum(expenses)  # 최대 인출액은 모든 지출 합
answer = right

while left <= right:
    mid = (left + right) // 2
    if can_withdraw(mid):
        answer = mid      # 가능하면 최소값 갱신
        right = mid - 1
    else:
        left = mid + 1

print(answer)
