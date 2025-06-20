import sys
import pprint

def solution(numbers, N):
    # dp[i][j]: numbers[i-1:j]의 팰린드롬 여부 저장. 
    # 팰린드롬 이면 1, 아니면 0
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1): # 길이 1
        dp[i][i] = 1
    
    for i in range(1, N): # 길이 2
        if numbers[i - 1] == numbers[i]:
            dp[i][i + 1] = 1

    for length in range(3, N + 1): # 길이 3 이상
        for start in range(1, N - length + 2):
            end = start + length - 1
            if dp[start + 1][end - 1] == 0:
                continue
            if numbers[start - 1] == numbers[end - 1]:
                dp[start][end] = 1

    return dp

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    numbers = list(map(int, input().split()))
    dp = solution(numbers, N)
    
    M = int(input())
    for _ in range(M):
        s, e = map(int, input().split())
        print(dp[s][e])