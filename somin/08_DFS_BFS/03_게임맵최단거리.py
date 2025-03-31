from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque([(0,0)])
    visited = set([(0, 0)])  # 방문한 좌표 저장
    
    # 상, 하, 좌, 우 이동 방향
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while q:
        curr_r, curr_c = q.popleft()

        for r, c in directions:
            next_r =  curr_r + r
            next_c = curr_c + c

            # 범위 내에 있고, 이동 가능한 경로(1)이며, 방문하지 않은 경우
            if (
                0 <= next_r < n and
                0 <= next_c < m and
                maps[next_r][next_c] == 1 and
                (next_r, next_c) not in visited
            ):
                # 이전 위치에서 +1 한 값으로 거리 갱신
                maps[next_r][next_c] = maps[curr_r][curr_c] + 1
                visited.add((next_r, next_c))
                q.append((next_r, next_c))

    # 도착 지점이 visited에 없다면 도달 불가능
    return maps[n-1][m-1] if (n-1, m-1) in visited else -1

if __name__ == "__main__":
    maps = [[1,0,1,1,1],
            [1,0,1,0,1],
            [1,0,1,1,1],
            [1,1,1,0,1],
            [0,0,0,0,1]]
    
    print(solution(maps))  