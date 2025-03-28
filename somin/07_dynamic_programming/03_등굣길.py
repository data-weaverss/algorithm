def solution(m, n, puddles):
    """집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return"""

    # 2차원 DP 테이블 초기화 (n+1) x (m+1)
    map = [[0] * (m + 1) for _ in range(n + 1)]

    # 웅덩이 위치
    puddle_set = set((y, x) for x, y in puddles)
    map[1][1] = 1 # 출발 지점

    for i in range(1, n + 1):   # 행
        for j in range(1, m + 1): # 열
            if (i, j) in puddle_set:
                map[i][j] = 0  # 웅덩이는 경로가 없으므로 0으로 설정
                continue
            map[i][j] += map[i - 1][j]  # 위에서 오는 경로
            map[i][j] += map[i][j - 1]  # 왼쪽에서 오는 경로
     
    return map[n][m] % 1000000007

if __name__ == "__main__":
    m, n = 4, 3
    puddles = [[2, 2]]

    print(solution(m, n, puddles))  # 4