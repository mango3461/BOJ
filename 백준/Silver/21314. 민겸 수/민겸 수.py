import sys

s = sys.stdin.readline().strip()

max_res, min_res = "", ""
cnt_m = 0

for ch in s:
    if ch == 'M':
        cnt_m += 1
    else:  # ch == 'K'
        # 최대값
        max_res += '5' + '0' * cnt_m
        # 최소값
        min_res += '1' + '0' * (cnt_m - 1) + '5' if cnt_m > 0 else '5'
        cnt_m = 0

# 마지막 M 처리
if cnt_m > 0:
    max_res += '1' * cnt_m
    min_res += '1' + '0' * (cnt_m - 1)

print(max_res)
print(min_res)
