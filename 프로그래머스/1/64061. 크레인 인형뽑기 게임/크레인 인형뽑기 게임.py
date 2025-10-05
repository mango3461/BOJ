def solution(board, moves):
    n = len(board)
    columns = [[] for _ in range(n)]
    
    for c in range(n):
        for r in range(n-1, -1, -1):
            if board[r][c] != 0:
                columns[c].append(board[r][c])
                
    basket = []
    answer = 0
    
    
    for move in moves:
        col = move - 1
        if columns[col]:
            doll = columns[col].pop()
            if basket and basket[-1] == doll:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)
    return answer