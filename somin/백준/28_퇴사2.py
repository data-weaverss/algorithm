import sys

def solution(N, schedule):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        # i일까지의 최대 수익을 이전 값으로 갱신
        dp[i] = max(dp[i], dp[i - 1])

        # 현재 날짜의 상담 정보
        time, pay = schedule[i - 1]
        end_date = i + time - 1 # 상담 종료 날짜

        # 상담이 퇴사 전 완료되는 경우에만 처리
        if end_date <= N:
            # 해당 날짜에 도달 가능한 최대 수익 갱신
            dp[end_date] = max(dp[end_date], dp[i - 1] + pay)
    
    return dp[N]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    schedule = []
    for _ in range(N):
        T, P = map(int, sys.stdin.readline().split())
        schedule.append((T, P))
    
    print(solution(N, schedule))