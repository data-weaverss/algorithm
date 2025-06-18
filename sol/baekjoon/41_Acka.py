import sys

MOD = 1000000007

# dp[n][a][b][c] 메모이제이션 테이블 (-1로 초기화)
# dp[song_cnt][d][k][h]
#    : song_cnt 개의 곡을 남겨두고, d곡,k곡,h곡 남겨야 할 때 가능한 방법의 수
dp = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

def solution(song_cnt, d, k, h):
    """ 
    d, k, h 중 적어도 한 명이 불러야 함
    녹음해야 하는 곡 song_cnt에서, 앨범을 만들 수 있는 방법의 수를 반환
    
    1 <= song_cnt <= 50
    1 <= d, k, h <= song_cnt
    
    총 시간 복잡도:  O(song_cnt * d * k * h) = 10^6
    핵심 아이디어: 
    - 각 노래마다 (i, j, l)의 조합으로 누가 노래를 부를지를 결정
    """ 
    if d < 0 or k < 0 or h < 0:
        return 0
    
    # 모든 곡을 다 불렀을 때, 남은 곡 수도 0이면 valid
    if song_cnt == 0:
        return 1 if d == 0 and k == 0 and h == 0 else 0
    
    # 이미 계산한 상태면 메모이제이션 반환
    if dp[song_cnt][d][k][h] != -1:
        return dp[song_cnt][d][k][h]
    
    dp[song_cnt][d][k][h] = 0
    
    # 한 곡을 d, k, h 중 최소 1명, 최대 3명 불러야 함
    for i in (0, 1):
        for j in (0, 1):
            for l in (0, 1):
                if i + j + l == 0: # (0, 0, 0)은 제외하고
                    continue
                dp[song_cnt][d][k][h] += solution(song_cnt - 1, d - i, k - j, h - l)
                dp[song_cnt][d][k][h] %= MOD

    return dp[song_cnt][d][k][h]

if __name__ == "__main__":
    input = sys.stdin.readline
    inputs = list(map(int, input().split()))
    
    if inputs[0] > sum(inputs[1:]): 
        print(0) 
    else:
        print(solution(inputs[0], inputs[1], inputs[2], inputs[3]))
