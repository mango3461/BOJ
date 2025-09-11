import sys
input = sys.stdin.readline

# 수열 A 입력
N = int(input())
A = list(map(int, input().split()))

# 수열 A 정렬
A.sort()

# 확인할 수 X 입력
M = int(input())
X_list = list(map(int, input().split()))

# 이진 탐색 함수
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# 각 X에 대해 수열 A에 존재하는지 확인
for x in X_list:
    if binary_search(A, x):
        print(1)
    else:
        print(0)