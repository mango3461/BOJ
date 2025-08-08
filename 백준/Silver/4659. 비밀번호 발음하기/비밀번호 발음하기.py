import sys
input = sys.stdin.readline

def is_acceptable(pw):
    aeiou = set('aeiou')
    # 모음 포함 여부
    if not any(ch in aeiou for ch in pw):
        return False
    
    # 모음/자음 3개 연속 확인
    count = 0
    prev_is_aeiou = None
    
    for ch in pw:
        if ch in aeiou:
            if prev_is_aeiou == True:
                count += 1
            else:
                count = 1
            prev_is_aeiou = True
        else:
            if prev_is_aeiou == False:
                count += 1
            else:
                count = 1
            prev_is_aeiou = False
        
        if count >= 3:
            return False
    
    # 같은 글자 연속 금지(ee,oo 제외)
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1] and pw[i] not in ('e', 'o'):
            return False
        
    return True

while True:
    pw = input().strip()
    if pw == "end":
        break
        
    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")

