import sys
import pprint

def solution(N, matrix_dims):
    INF = float('inf')
    # dp[i][j] = 행렬 i~j까지 곱할 때의 최소 연산 횟수
    dp = [[INF] * N for _ in range(N)]

    for i in range(N): # 행렬 본인만 있을 때의 연산횟수
        dp[i][i] = 0

    for length in range(2, N + 1):
        for start in range(N - length + 1):
            end = start + length - 1
            for mid in range(start, end):
                cost = ( # 왼쪽 연산수 + 오른쪽 연산수 + 두 행렬 곱셈 연산수
                    dp[start][mid] + 
                    dp[mid + 1][end] + 
                    matrix_dims[start][0] * matrix_dims[mid][1] * matrix_dims[end][1]
                )
                dp[start][end] = min(dp[start][end], cost)

    return dp[0][N - 1]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    matrix_dims = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution(N, matrix_dims))