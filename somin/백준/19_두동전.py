import sys
from collections import deque

def solution(board, n, m):
    """
    두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
    """

    # 동전의 현재 위치찾기
    coins = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'o':
                coins.append((i, j))    

    directions = [[0, -1], [0, 1], [1, 0] , [-1, 0]] # 왼, 오, 위, 아래
    visited = set()
    queue = deque([(coins[0], coins[1], 0)])  # coin1, coin2, 이동 횟수

    while queue:
        c1, c2, count = queue.popleft()
        if count >= 10:
            return -1

        for dr, dc in directions:
            nc1 = (c1[0]+dr, c1[1]+dc)
            nc2 = (c2[0]+dr, c2[1]+dc)
            
            nc1_fall = not (0 <= nc1[0] < n and 0 <= nc1[1] < m)
            nc2_fall = not (0 <= nc2[0] < n and 0 <= nc2[1] < m)

            if nc1_fall and nc2_fall: # 둘 다 떨어지는 경우
                continue
            if nc1_fall or nc2_fall: # 하나만 떨어지는 경우
                return count + 1
            
            # 벽을 만났을 때, 
            if board[nc1[0]][nc1[1]] == '#':
                nc1 = c1
            if board[nc2[0]][nc2[1]] == '#':
                nc2 = c2

            if (nc1, nc2) not in visited:
                visited.add((nc1, nc2))
                queue.append((nc1, nc2, count+1))
                
    return -1


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    
    board = []
    for _ in range(n):
        row = list(sys.stdin.readline().strip())
        board.append(row)

    print(solution(board, n, m))