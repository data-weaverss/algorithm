import sys

def solution(n, k, coins):
    INF = float('inf')
    dp = [INF] * (k + 1) # i금액을 만들기 위한 최소 동전 개수
    dp[0] = 0 
    
    for coin in coins:
        for amount in range(coin, k + 1):
            # coin을 썼을 때의 최소 개수로 갱신
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[k] if dp[k] != INF else -1

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline()) for _ in range(n)]

    print(solution(n, k, coins))
