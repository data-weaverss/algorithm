"""
규칙: 한번에 하나씩, 조각 회전 O, 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안됨
Args
    game_board: 현재 게임 보드의 상태
    table: 테이블 위에 놓인 퍼즐 조각의 상태
Returns
    규칙에 맞게 최대한 많은 퍼즐 조각을 채워 넣을 경우, 총 몇 칸을 채울 수 있는지
"""

from collections import defaultdict

def dfs(map, moves, n, cur_row, cur_col, routes):
    routes.append((cur_row, cur_col))
    for move_row, move_col in moves:
        new_row, new_col = cur_row + move_row, cur_col + move_col
        if 0 <= new_row < n and 0 <= new_col < n:
            if map[new_row][new_col] == 1 and (new_row, new_col) not in routes:
                dfs(map, moves, n, new_row, new_col, routes)    

def extract_puzzle(map, routes):
    """주어진 좌표를 기반으로 퍼즐 조각 추출"""
    row1, row2 = min(r[0] for r in routes), max(r[0] for r in routes)
    col1, col2 = min(r[1] for r in routes), max(r[1] for r in routes)
    
    puzzle = [[0] * (col2 - col1 + 1) for _ in range(row2 - row1 + 1)]
    for row, col in routes:
        puzzle[row - row1][col - col1] = 1
        map[row][col] = 0
    return puzzle

def generate_rotations(puzzle):
    """퍼즐 조각의 모든 회전(90도씩)을 생성"""
    rotations = [puzzle]
    for _ in range(3):  # 총 3번 회전하여 90도씩 추가
        rotated = [list(x) for x in zip(*rotations[-1])][::-1]
        rotations.append(rotated)
    return rotations

def normalize_puzzle(puzzle):
    """퍼즐을 문자열로 변환하여 비교 가능하게 만듦"""
    return str(puzzle)
    
def solution(game_board, table):
    n = len(table)
    moves = ((-1, 0), (1, 0), (0, 1), (0, -1))
    table_puzzles, board_puzzles = [], []
    
    # game_board 에서 빈칸을 퍼즐이라 생각하고,
    # game_board의 퍼즐과 table의 퍼즐 중 몇개가 일치하는지 찾는 것으로 접근
    for i in range(n): # game_board 0, 1 반전 -> 빈칸을 퍼즐로 여기도록 반전시킴
        for j in range(n):
            game_board[i][j] = 1 - game_board[i][j]
    
    for row in range(n):
        for col in range(n):
            if table[row][col] == 1:  # 테이블에서 퍼즐 찾기
                routes = []
                dfs(table, moves, n, row, col, routes)
                puzzle = extract_puzzle(table, routes)
                table_puzzles.append([normalize_puzzle(rot) for rot in generate_rotations(puzzle)])
            if game_board[row][col] == 1:  # 게임 보드에서 빈 공간 찾기
                routes = []
                dfs(game_board, moves, n, row, col, routes)
                puzzle = extract_puzzle(game_board, routes)
                board_puzzles.append(normalize_puzzle(puzzle))
    
    # 게임 보드 퍼즐 카운트 저장
    board_puzzles_count = defaultdict(int)
    for board_puzzle in board_puzzles:
        board_puzzles_count[board_puzzle] += 1
    
    answer = 0
    for puzzle in table_puzzles:
        for rotation in puzzle:
            if board_puzzles_count.get(rotation, 0) > 0:
                answer += rotation.count('1')
                board_puzzles_count[rotation] -= 1
                break

    return answer

if __name__ == "__main__":
    game_board = [
        [1,1,0,0,0],
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,1,1,0],
        [1,1,1,1,1]
    ]
    table = [
        [1,0,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,0]
    ]
    print(solution(game_board, table))