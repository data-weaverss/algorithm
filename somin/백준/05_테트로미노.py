import sys

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 'ㅗ' 모양 상대 좌표
t_shapes = [
    [(-1, 0), (0, -1), (0, 1)],  # ㅗ
    [(1, 0), (0, -1), (0, 1)],   # ㅜ
    [(0, -1), (-1, 0), (1, 0)],  # ㅓ
    [(0, 1), (-1, 0), (1, 0)]    # ㅏ
]

def dfs(x, y, depth, total):
    """DFS를 사용하여 연속된 4칸의 최대 합을 계산"""
    global max_value

    if depth == 4:
        max_value = max(max_value, total)
        return

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M \
              and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False  # 백트래킹

def check_t_shape(x, y):
    """'ㅗ' 모양을 포함한 예외적인 모양의 최대 합을 계산"""
    global max_value

    for shape in t_shapes:
        total = board[x][y]
        valid = True
        for dx_, dy_ in shape:
            nx, ny = x + dx_, y + dy_
            if 0 <= nx < N and 0 <= ny < M:
                # 좌표가 보드 범위 내에 있다면
                total += board[nx][ny]
            else:
                valid = False
                break
        if valid:
            max_value = max(max_value, total)

if __name__ == "__main__":
    global board, visited, max_value

    sys.setrecursionlimit(10000)
    input_data = list(map(int, sys.stdin.read().split()))

    # 보드 생성
    N, M = input_data[0], input_data[1]
    board = [input_data[i*M+2 : (i+1)*M+2] for i in range(N)]

    # 방문 여부 초기화
    visited = [[False] * M for _ in range(N)]
    max_value = 0

    # 모든 좌표를 시작점으로 탐색
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, board[i][j])
            visited[i][j] = False
            check_t_shape(i, j)

    print(max_value)