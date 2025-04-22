from collections import deque, defaultdict
def solution(game_board, table):
    """
    Parameters:
        - game_board (List[int]): 현재 게임 보드의 상태
        - table (List[int]): 테이블 위에 놓인 퍼즐 조각의 상태
    Returns:
        - 규칙에 맞게 최대한 많은 퍼즐 조각을 채워 넣을 경우, 총 몇 칸을 채울 수 있는지 (int)
    rule:
        - 조각 회전 O, 반전 X
        - 게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됨.
    """
    queue = deque([[(0,0)]]) # 행,열,조각좌표
    visited = set()
    puzzle = defaultdict(list)
    direct = [(0,1), (0,-1), (-1,0), (1,0)] # 동서남북 방향
    n = len(game_board)
    # print(queue)

    while queue:
        print(queue)
        
        path = queue.popleft()
        r, c = path[-1]
        if (r, c) == (0,0) and game_board[r][c] != 0:
            path = []
        
        for i, j in direct:
            if 0 <= r + i < n and 0 <= c + j < n and game_board[r+i][c+j] == 0:
                path.append((r+i, c+j))
                queue.append(path)
                game_board[r+i][c+j] = 1
        
        # if q_length == len(queue):
            # 사방으로 갈 수 없다면 해당 퍼증 저장
        break
    print(queue)
                
    return -1

if __name__ == "__main__":
    game_board = [[1,1,0,0,1,0],
                  [0,0,1,0,1,0],
                  [0,1,1,0,0,1],
                  [1,1,0,1,1,1],
                  [1,0,0,0,1,0],
                  [0,1,1,1,0,0]]
    table = [[1,1,0,0,1,0],
             [0,0,1,0,1,0],
             [0,1,1,0,0,1],
             [1,1,0,1,1,1],
             [1,0,0,0,1,0],
             [0,1,1,1,0,0]]
    
    print(solution(game_board, table)) # 14