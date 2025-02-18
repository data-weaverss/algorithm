# 연속된 숫자 제거 단, 순서는 유지
def solution(arr):
    s = [-1] # 스택 초기화
    for i in arr:
        if s[-1] == i: continue
        s.append(i)
    
    return s[1:]

if __name__ == "__main__":
    arr = [1,1,3,3,0,1,1]
    sol = solution(arr)
    print(sol)