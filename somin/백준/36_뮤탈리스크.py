import sys
from itertools import permutations

def solution(SCV):
    MAX = 61
    INF = float('inf')

    dp = [[[INF] * MAX for _ in range(MAX)] for _ in range(MAX)]
    damages = list(permutations([9, 3, 1], 3)) # 공격 데미지 순열

    SCV += [0] * (3 - len(SCV))
    a, b, c = SCV
    dp[a][b][c] = 0
    
    # 모든 상태를 완전탐색
    for i in range(a, -1, -1):
        for j in range(b, -1, -1):
            for k in range(c, -1, -1):
                if dp[i][j][k] == INF:
                    continue
                for dmg in damages:
                    ni = max(0, i - dmg[0])
                    nj = max(0, j - dmg[1])
                    nk = max(0, k - dmg[2])
                    dp[ni][nj][nk] = min(dp[ni][nj][nk], dp[i][j][k] + 1)

    return dp[0][0][0]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    SCV = list(map(int, sys.stdin.readline().split()))
    print(solution(SCV))