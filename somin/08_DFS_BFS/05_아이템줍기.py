from collections import deque

def make_board(rectangle):
    board = [[0]*102 for _ in range(102)]

    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = -1  # 내부
                elif board[i][j] != -1:
                    board[i][j] = 1   # 테두리
    return board

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = make_board(rectangle)
    visited = [[0]*102 for _ in range(102)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_x, start_y = characterX * 2, characterY * 2
    end_x, end_y = itemX * 2, itemY * 2

    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while q:
        x, y = q.popleft()

        if (x, y) == (end_x, end_y):
            return (visited[x][y] - 1) // 2  # 거리 보정

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

if __name__ == "__main__":
    rectangle = [
        [1,1,4,4],  # 큰 사각형
        [2,2,3,3],  # 안에 작은 사각형 (겹침)
    ]
    characterX, characterY = (1, 1)
    itemX, itemY = (4, 4)

    print(solution(rectangle, characterX, characterY, itemX, itemY))  # 출력: 17
