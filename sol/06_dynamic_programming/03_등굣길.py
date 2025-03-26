def count_paths(cur_row, cur_col, memo, moves):
    # 이미 계산된 경로 수가 있다면 그 값을 반환
    if memo[cur_row][cur_col] != 0:
        return memo[cur_row][cur_col]
    
    # 각 방향(위, 왼쪽) 에서 현재 위치로 오는 경로 수를 더해줌
    for move_row, move_col in moves:
        next_row, next_col = cur_row + move_row, cur_col + move_col
        
        # 지도 범위 안에 있고, 웅덩이가 아닌 경우만 진행
        if 1 <= next_row < len(memo) and 1 <= next_col < len(memo[0]):
            if memo[next_row][next_col] == -1:
                continue
            memo[cur_row][cur_col] += count_paths(next_row, next_col, memo, moves)
    
    return memo[cur_row][cur_col]

def solution(m, n, puddles):
    """
    - 아래, 위로만 움직이는 경우 = 어떤 경로든 최단 경로임
    Args:
        - m: 가로길이(열 수), n: 세로길이(행 수)
        - puddles: 물에 잠긴 지역의 좌표
    Returns:
        - 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수 % 1000000007
    """
    MOD = 1000000007

    # memo[row][col] = (1, 1)부터 (row, col) 까지의 경로 수
    memo = [[0] * (m+1) for _ in range(n+1)]
    
    # 시작 지점(home) 초기화
    memo[1][1] = 1 
    
    # 웅덩이 표시
    for puddle_col, puddle_row in puddles:
        memo[puddle_row][puddle_col] = -1
    
    # 위쪽과 왼쪽 방향만 탐색(Top-Down)
    directions = [(-1, 0), (0, -1)]
    
    # 학교 위치에서 경로 계산 시작
    count_paths(n, m, memo, directions)

    # top down                
    return memo[n][m] % MOD

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2, 2]]
    print(solution(m, n, puddles)) 