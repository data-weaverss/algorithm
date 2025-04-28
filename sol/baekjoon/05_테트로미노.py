import sys

def solution(n, m, grid):
    """
    세로 n, 가로 m 
    테트로미노가 놓인 칸에 쓰여 있는 수들의 최댓값 반환
    """  
    moves = [(1, 0), (0, 1)]
    totals = []
    visited = []
    stack = []
    for row in range(n):
        for col in range(m):
            stack.append([[(row, col)], grid[row][col]])
    stack = stack[::-1]
    while stack:
        routes, total = stack.pop()
        if routes in visited:
            continue
        visited.append(routes)
        if len(routes) == 4:
            totals.append((routes, total))
        else:
            for drow, dcol in moves:
                for route in routes:
                    cur_row, cur_col = route
                    new_row, new_col = cur_row + drow, cur_col + dcol
                    if 0 <= new_row < n and 0 <= new_col < m:
                        if (new_row, new_col) not in routes:
                            stack.append((set((new_row, new_col)) + routes, total + grid[new_row][new_col]))
                    
    totals.sort(key=lambda key: -key[1])
    
    return totals[0][1]
if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = tuple(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, grid))