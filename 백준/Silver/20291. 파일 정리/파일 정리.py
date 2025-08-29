from collections import Counter

n = int(input())  # 파일의 개수
extensions = [input().split('.')[1] for _ in range(n)]  # 확장자 추출

# 확장자별 개수 세기
ext_count = Counter(extensions)

# 사전순으로 정렬하여 출력
for ext in sorted(ext_count):
    print(ext, ext_count[ext])
