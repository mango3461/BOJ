import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

# lower_bound: target 이상인 첫 번째 인덱스
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# upper_bound: target 초과인 첫 번째 인덱스
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

for _ in range(M):
    a, b = map(int, input().split())
    left_idx = lower_bound(numbers, a)
    right_idx = upper_bound(numbers, b)
    count = right_idx - left_idx
    print(count)
