def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i in range(n):
        # 현재 가격이 이전보다 낮으면
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 끝까지 안 떨어진 경우 처리
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer
