def solution(money):
    """
    인접한 두 집을 털면 경보가 울림
    마을의 모든 집들은 동그랗게 배치되어 있음
    Args:
    - money: 각 집에 있는 돈이 담긴 배열
    Returns:
    - 훔칠 수 있는 돈의 최댓값
    """
    max_dp = [[0] * len(money) for _ in range(len(money))]
    
    for i in range(len(money)):
        max_dp[i][i] = money[i]
        
    for i in range(len(money)):
        for j in range(i+2, len(money)):
            if i == 0 and j == len(money) - 1:
                break
            max_dp[i][j] = max(max_dp[i][max(j-3, i)], max_dp[i][j-2]) + max_dp[j][j]
    
    answer = 0
    for i in range(len(max_dp)):
        answer = max(answer, max(max_dp[i]))
    
    return answer

if __name__ == "__main__":
    money = [1, 0, 8, 5, 3, 7, 3]
    print(solution(money)) #15