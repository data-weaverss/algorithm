import sys

def solution(board, N):
    """
    [0,0] > [N-1, N-1] 까지의 이동 경로 수
    """
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1

    for r in range(N):
        for c in range(N):
            if dp[r][c] == 0 or board[r][c] == 0:
                # 갈 수 없는 칸 건너뛰기, 마지막칸 중복 제거
                continue
            move = board[r][c]
            if r + move < N: # 오른쪽으로 이동
                dp[r + move][c] += dp[r][c]
            if c + move < N: # 아래쪽로 이동 
                dp[r][c + move] += dp[r][c]
    
    return dp[N-1][N-1]

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    print(solution(board, N))