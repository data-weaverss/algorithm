import sys
from collections import defaultdict

def solution(n, passengers, max_trains):
    """ 
    소형 기관차 3대를 이용하여 최대로 운송할 수 있는 손님 수
    - 각 소형 기관차는 번호가 연속적으로 이어진 객차를 끌게 함
    
    n <= 50,000
    passengers <= 100
    max_trains < n / 3
    
    총 시간 복잡도:  
    핵심 아이디어: 
        - 누적합을 활용해 구간합을 O(1)로 빠르게 계산
        - dp[train][j]: train번째 기관차가 j번째 객차까지 고려했을 때 운송할 수 있는 최대 승객 수
        - 점화식: 
        dp[train][j] = max(
            dp[train][j - 1],                        ← 이전 객차까지의 최댓값 유지
            dp[train - 1][j - max_trains] + curr_sum ← 현재 train이 맡을 구간 포함
        )
    """ 
    # dp[train][j] : train 번째 기관차가 j번째 객차까지 고려했을 때 최대 손님 수
    dp = list([0] * (n + 1) for _ in range(4))
    
    cum_sum = [0] * (n + 1)
    for i in range(n):
        cum_sum[i + 1] = cum_sum[i] + passengers[i]
        
    for train in range(1, 4):
        for j in range(train * max_trains, n+1):
            # 현재 기관차가 끄는 구간 [j - max_trains + 1, j]의 손님 수
            curr_sum = cum_sum[j] - cum_sum[j - max_trains]
            
            # 이전까지의 최대 vs 현재 구간 포함한 새로운 조합 중 큰 값 저장
            dp[train][j] = max(
                dp[train][j-1], 
                dp[train-1][j-max_trains] + curr_sum  # 현재 train이 새로운 구간을 맡음
            )
            
    return dp[3][n]

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    passengers = list(map(int, input().split()))
    max_trains = int(input())

    print(solution(n, passengers, max_trains))
