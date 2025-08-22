import sys

input = sys.stdin.readline

max_n = 100

dp = [0] * (max_n + 1)

dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6, max_n + 1):
    dp[i] = dp[i - 1] + dp[i - 5]

T = int(input())

for _ in range(T):
    N = int(input())
    print(dp[N])