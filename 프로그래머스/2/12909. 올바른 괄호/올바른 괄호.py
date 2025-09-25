from collections import deque
import sys

s = sys.stdin.readline

def solution(s):
    stack = deque()
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0