import sys
sys.setrecursionlimit(10**6)

MOD = 10**9 + 7

def solution(S, A, B, C):
    """
    앨범을 만드는 경우의 수
    → 곡마다 누가 참여하는지 다른 경우는 다른 앨범
    → 답을 1,000,000,007 로 나눈 나머지 출력
    
    - 가수 3명이 앨범을 녹음하려고 함
    - 총 S곡을 녹음해야 함
    - 각 가수가 반드시 몇 곡을 불러야 하는지 주어짐 → A, B, C
    - 각 곡은 1명 이상이 참여해야 하고,
      → 1명, 2명, 3명이 같이 불러도 됨
    """
    # dp[s][a][b][c] = s개의 곡을 남기고
    # a, b, c 개의 곡을 각 가수가 남겼을 때 앨범 만들 수 있는 경우의 수
    dp = [[[[-1 for _ in range(C+1)] for _ in range(B+1)] for _ in range(A+1)] for _ in range(S+1)]

    def dfs(s, a, b, c):
        # 곡을 모두 다 정했을 때
        if s == 0:
            if a == b == c == 0:
                return 1  # 성공한 경우
            else:
                return 0  # 실패한 경우 (남은 곡 있음)

        # 이미 계산한 경우
        if dp[s][a][b][c] != -1:
            return dp[s][a][b][c]

        res = 0

        # 가능한 7가지 조합 
        for i in range(2):  # a 참여 여부 (0 or 1)
            for j in range(2):  # b 참여 여부
                for k in range(2):  # c 참여 여부
                    if i == j == k == 0:
                        continue  # 최소 한 명은 참여해야 함

                    # 해당 조합으로 곡 참여 가능한가?
                    if a - i >= 0 and b - j >= 0 and c - k >= 0:
                        res = (res + dfs(s - 1, a - i, b - j, c - k)) % MOD # 경우의 수 누적

        dp[s][a][b][c] = res
        return res

    return dfs(S, A, B, C)

if __name__ == "__main__":
    S, A, B, C = map(int, sys.stdin.readline().split())
    print(solution(S, A, B, C))
