import sys

""" 
    특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정
    
    3 <= region_cnt <= 10^4
    1 <= budget <= 10^5
    region_cnt <= budgets_sum <= 10^9
        
    총 시간 복잡도: O(region_cnt log(budget))
    핵심 아이디어: 이진탐색
""" 
def solution(region_cnt, budgets, budgets_sum):
    budgets.sort()
    
    if sum(budgets) <= budgets_sum: return budgets[-1]
    
    left = 0
    right = budgets[-1]
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # 현재 상한액(mid)을 기준으로 총 배정 예산 계산
        total = sum(b if b <= mid else mid for b in budgets)
        
        if total <= budgets_sum:
            # 배정 총액이 예산 한도 이하면, 상한액을 더 높일 수 있음
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    budgets = list(map(int, input().split()))
    m = int(input())
    print(solution(n, budgets, m))
