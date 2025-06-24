import sys

def solution(budgets, total_budget, N):
    """
    N개 지방에서 각각 예산 요청 (budgets 리스트)한다.
    총 예산(total_budget)에 맞추어 최대로 예산을 배정했을 경우, 최대 예산금액을 구하라.
    규칙:
    - 만약 총합을 초과한다면 상한액을 정해야 함.

    1. 예산 요청을 오름차순 정렬
    2. 작은 것부터 처리
    3. 남은 예산을 균등분배(mean_budget)로 계산하여 상한을 결정하는 구조
    """
    # 그대로 다 배정 가능한 경우
    if sum(budgets) <= total_budget:
        return max(budgets)
    
    # 예산 초과 시 → 상한을 결정해야 함
    budgets.sort()
    for i in range(N):
        # 모든 지역을 균등하게 나누었을 때의 금액 = 상한액
        mean_budget = int(total_budget / (N - i))
        if budgets[i] <= mean_budget:
            total_budget -= budgets[i]
        else:
            return mean_budget

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    budgets = list(map(int, sys.stdin.readline().split()))
    total_budget = int(sys.stdin.readline())

    print(solution(budgets, total_budget, N))