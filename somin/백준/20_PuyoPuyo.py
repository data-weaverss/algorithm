import sys
from collections import deque
import pprint

def apply_gravity(board):
    """각 열에 대해 '.'이 아닌 블록을 아래로 이동"""
    for col in range(6):
        new_col = []
        for row in range(12):
            if board[row][col] not in ('.', 'x'):
                new_col.append(board[row][col])
                
        new_col = ['.'] * (12 - len(new_col)) + new_col
        for row in range(12):
            board[row][col] = new_col[row]

    return board

def bfs(start, color, board, visited):
    """(row, col)에서 시작하는 같은 색 블록 그룹 탐색"""
    queue = deque([start])
    connected_blocks = [start] # 연결된 블록 위치 저장
    visited.add(start) # 방문 기록

    directions = [(1,0), (-1,0), (0,-1), (0,1)] # 상하좌우

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 12 and 0 <= nc < 6:
                if (nr, nc) not in visited and board[nr][nc] == color:
                    visited.add((nr, nc))
                    connected_blocks.append((nr, nc))
                    queue.append((nr, nc))
    
    return connected_blocks


def solution(board):
    """
    전체 보드를 순회하며 같은 색 뿌요 4개 이상 연결된 그룹을 찾아
    동시에 터뜨리고, 중력 적용 후 연쇄 반응 수를 반환
    """
    chain_count = 0  # 연쇄 횟수

    while True:
        visited = set()
        to_pop = set()

        # 보드 전체 탐색하여 터뜨릴 블록 그룹 수집
        for r in range(12):
            for c in range(6):
                if board[r][c] != '.' and (r, c) not in visited:
                    group = bfs((r, c), board[r][c], board, visited)
                    if len(group) >= 4:
                        to_pop.update(group)

        # 터뜨릴 블록이 없으면 종료
        if not to_pop:
            break

        for r, c in to_pop:
            board[r][c] = '.'
        
        apply_gravity(board)  # 중력 작용
        chain_count += 1
            
    return chain_count


if __name__ == "__main__":
    board = [list(sys.stdin.readline().strip()) for _ in range(12)]
    print(solution(board))