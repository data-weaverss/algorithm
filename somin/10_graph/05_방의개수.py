from collections import defaultdict

def solution(arrows):
    """
    예외1. 간선을 중복하여 되돌아 오는 경우 - 방이 생성되면 안됨
    예외2. 대각선을 가로질러 방이 2개 생기는 경우
    """
    visited = defaultdict(list)
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    x, y = 0, 0 # 원점
    cycle = 0

    for arrow in arrows:
        for _ in range(2): # 대각선 교차점을 정점으로 만들기 위해 두칸 이동
            nx = x + dx[arrow]
            ny = y + dy[arrow]

            if (nx, ny) in visited and (x, y) not in visited[(nx, ny)]: 
                # 방문했던 점이지만 경로가 겹치지 않는 경우
                cycle += 1    

            visited[(x, y)].append((nx, ny))
            visited[(nx, ny)].append((x, y))
            x, y = nx, ny

    return cycle

if __name__ == "__main__":
    # arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
    arrows = [1, 6, 4, 6, 1]
    print(solution(arrows))