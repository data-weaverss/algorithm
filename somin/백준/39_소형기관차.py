import sys

def solution(N, arr, M):
    # 누적합 계산
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]

    # dp[k][i]: k대의 기관차로 i번째 객차까지 고려했을 때 최대 승객 수
    dp = [[0] * (N + 1) for _ in range(4)] 

    for k in range(1, 4):  # 기관차 1~3대
        for i in range(M * k, N + 1):
            sum_m = prefix[i] - prefix[i - M]
            dp[k][i] = max(dp[k][i - 1], dp[k - 1][i - M] + sum_m)

    return dp[3][N]


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    print(solution(N, arr, M))
