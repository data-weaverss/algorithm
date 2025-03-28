def max_steal(money):
    n = len(money)
    if n == 0:
        return 0
    if n == 1:
        return money[0]
    
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    return dp[-1]

def solution(money):
    """도둑이 훔칠 수 있는 돈의 최댓값을 return 
    input:
        money: 각 집에 있는 돈이 담긴 배열
    condition:
        1. 모든 집들은 원형으로 배치
        2. 인접한 두 집을 털면 경보가 울림
    idea:
        dp - i번째 집까지의 최댓값을 저장. 현재 집을 털지 말지 결정하는 최적 선택을 누적하는 방식으로 채워나간다.
    """
    if len(money) == 1:
        return money[0]
    
    # 1. 첫 번째 집 포함, 마지막 집 제외
    case1 = max_steal(money[:-1])
    # 2. 첫 번째 집 제외, 마지막 집 포함
    case2 = max_steal(money[1:])
        
    return max(case1, case2)

if __name__ == "__main__":
    money = [1, 2, 3, 1]
    print(solution(money))  