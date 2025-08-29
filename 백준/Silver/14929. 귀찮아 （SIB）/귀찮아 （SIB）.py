from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

total = sum(arr)
squares = sum(x*x for x in arr)
res = (total*total - squares) // 2
print(res)
