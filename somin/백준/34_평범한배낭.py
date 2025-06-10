import sys

def solution(products, N, K):
    # 배낭의 최대 무게가 i일 때 얻을 수 있는 최대 가치
    dp = [0] * (K + 1)
    
    for weight, value in products:
        for i in range(K, weight - 1, -1):
            # 현재 무게 i에서 해당 물건을 선택했을 경우와 선택하지 않았을 경우를 비교
            dp[i] = max(dp[i], dp[i - weight] + value)
            
    return dp[K]

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    products = []
    for _ in range(N):
        products.append(list(map(int, sys.stdin.readline().split())))
    print(solution(products, N, K))