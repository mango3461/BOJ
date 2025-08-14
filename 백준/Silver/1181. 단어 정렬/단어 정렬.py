import sys
input = sys.stdin.readline

n = int(input())
strings = list(set(input().strip() for _ in range(n)))  # 중복 제거

length_buckets = {}

# 1. 길이별로 버킷 생성
for s in strings:
    length = len(s)
    if length not in length_buckets:
        length_buckets[length] = []
    length_buckets[length].append(s)

# 2. 각 버킷 안에서 알파벳 순 정렬
for bucket in length_buckets.values():
    bucket.sort()

# 3. 길이 순으로 결과 합치기 및 출력
for length in sorted(length_buckets):
    for word in length_buckets[length]:
        print(word)
