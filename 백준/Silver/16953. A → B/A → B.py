a, b = map(int, input().split())
count = 1  # 연산 횟수, 처음 B 상태 포함

while b > a:
    if b % 2 == 0:      # B가 짝수면 2로 나눔
        b //= 2
    elif b % 10 == 1:   # B가 1로 끝나면 마지막 1 제거
        b = (b - 1) // 10
    else:               # 더 이상 A로 만들 수 없으면 종료
        count = -1
        break
    count += 1

if b != a:
    count = -1

print(count)
