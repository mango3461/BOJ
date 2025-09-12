def solution(n):
    
    left = 0
    right = n // 2 + 2
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid == n:    
            return (mid+1)**2
        elif mid * mid < n: 
            left = mid + 1
        else:                 
            right = mid - 1
        
    return -1