import sys
from collections import deque, defaultdict

def get_max_length(board, n):
    """
    가장 긴 길이 반환
    """

    max_len = 1
    for i in range(n):
        row_cnt, col_cnt = 1, 1
        for j in range(n-1):
            # row 
            if board[i][j] == board[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            max_len = max(max_len, row_cnt)
            # col
            if board[j][i] == board[j+1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            max_len = max(max_len, col_cnt)
    
    return max_len

def solution(board, n):
    """
    Parameters:
        - n (int): 보드 크기
        - board (List[int]): n x n 보드
    Returns:
        - 한번 스왑 후?, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열) 최대 개수 (int)
    """
    answer = 0
    for i in range(n):
        for j in range(n):
            # 오른쪽 swap
            if j+1 < n:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                answer = max(answer, get_max_length(board, n))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]  # 되돌리기

            # 아래쪽 swap
            if i+1 < n:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                answer = max(answer, get_max_length(board, n))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 되돌리기
    return answer

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    board = []
    for _ in range(n):
        row = list(sys.stdin.readline().strip())
        board.append(row)

    print(solution(board, n))