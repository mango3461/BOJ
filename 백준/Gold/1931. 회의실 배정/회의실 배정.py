import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0

for start,end in arr:
    if start >= end_time:
        count += 1
        end_time =end
        
print(count)