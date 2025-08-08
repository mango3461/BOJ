import sys

input = sys.stdin.readline
s = input().strip()
open_stack = []
value_stack = []

for char in s:
    if char == '(' or char == '[':
        open_stack.append(char)
        value_stack.append(0)
    else:
        if not open_stack:
            print(0)
            sys.exit()
        elif (char == ')' and open_stack[-1] != '(') or (char == ']' and open_stack[-1] != '['):
            print(0)
            sys.exit()
        else:
            open_stack.pop()
            
            temp = 0
            while value_stack and value_stack[-1] != 0:
                temp += value_stack.pop()

            if value_stack:
                value_stack.pop()

            if temp == 0:
                if char == ')':
                    value_stack.append(2)
                else:
                    value_stack.append(3)
            else:
                if char == ')':
                    value_stack.append(temp * 2)
                else:
                    value_stack.append(temp * 3)

if open_stack:
    print(0)
    sys.exit()

print(sum(value_stack))
        
        
        
        