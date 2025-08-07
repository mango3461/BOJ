from collections import deque
import sys

input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    order = 0
    
    dq = deque((priority, idx) for idx, priority in enumerate(queue))
    
    while dq:
        max_priority = max(dq, key=lambda x: x[0])[0]
        
        if dq[0][0] < max_priority:
            dq.append(dq.popleft())
        else:
            priority, idx = dq.popleft()
            order += 1
            if idx == m:
                print(order)
                break
