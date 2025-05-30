import sys

def solution(N, consultations):
    """
    consultations: [[duration, reward], ...]
    - duration: 상담을 완료하는데 걸리는 기간
    - reward: 상담을 했을 때 받을 수 있는 금액
    
    얻을 수 있는 최대 수익을 반환
    
    1 <= N <= 1,500,000 = 10^6
    1 <= duration <= 50, 1 <= reward <= 1,000
    
    총 시간 복잡도: O(N)
    핵심 아이디어: DP + 현재까지의 최댓값 추적
    각 날짜별 최대 수익을 계산
    """  
    # dp[day] = 해당 날짜까지 얻을 수 있는 최대 수익
    # dp[2] = 3이면 2일차를 끝까지 써야 받을 수 있는 최대 수익
    dp = [0] * (N) # 0일부터 N-1일까지 
    cur_max = 0 # 현재까지의 최대 누적 수익
    
    for day in range(N):
        duration, reward = consultations[day]
        end_day = day + duration - 1 # 상담이 끝나는 날 계산
        
        if end_day < N: # 상담이 기간 내에 완료되는 경우만 처리
            # 기존 end_day의 최댓값 vs 현재까지 최대 수익 + 현재 상담 보상
            dp[end_day] = max(dp[end_day], cur_max + reward)
        
        # 이전 최대 수익 vs 오늘까지 마무리된 상담의 최대 수익 
        cur_max = max(cur_max, dp[day])
        
    return cur_max
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    TP = [list(map(int, input().split())) for _ in range(N)]
    
    print(solution(N, TP))
