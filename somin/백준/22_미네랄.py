import sys
from collections import deque
import pprint

def bfs(cave, R, C, start, visited):
    """연결된 미네랄 클러스터 탐색 (BFS)"""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    q = deque([start])
    cluster = [start]
    visited.add(start)

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                if cave[nr][nc] == 'x':
                    visited.add((nr, nc))
                    cluster.append((nr, nc))
                    q.append((nr, nc))        
                        
    return cluster

def apply_gravity(cave, R, C, floating_cluster):
    """공중에 떠 있는 클러스터에 중력 적용"""

    # 열별로 가장 아래에 있는 미네랄 좌표 수집
    bottom_by_col = []
    floating_cluster.sort(key=lambda x: (x[1], -x[0]))  # 열 기준 정렬 (아래부터 우선)

    bottom_row = floating_cluster[0][0]
    current_col = floating_cluster[0][1]
    for r, c in floating_cluster:
        if c == current_col:
            if r > bottom_row:
                bottom_row = r
        else:
            bottom_by_col.append((bottom_row, current_col))
            bottom_row, current_col = r, c
    bottom_by_col.append((bottom_row, current_col))  # 마지막 열 추가

    # 바닥 또는 다른 클러스터까지의 최소 거리 계산
    min_fall_dist = R
    for r, c in bottom_by_col:
        for fall_r in range(r + 1, R):
            if cave[fall_r][c] == 'x':
                min_fall_dist = min(min_fall_dist, fall_r - r - 1)
                break
        else:
            min_fall_dist = min(min_fall_dist, R - r - 1)
    
    # 클러스터 제거 후 새로운 위치에 재배치
    floating_cluster.sort(reverse=True)  # 위에서부터 덮지 않도록 정렬
    for r, c in floating_cluster:
        cave[r][c] = '.'
    for r, c in floating_cluster:
        cave[r + min_fall_dist][c] = 'x'

def solution(cave, R, C, N, rows_to_remove):
    """
    RxC 동굴에서 미네랄을 N번 제거하고, 중력을 적용한 뒤 동굴 상태를 출력하시오.

    클러스터: 상하좌우 인접 미네랄 그룹. 
    규칙:
    1. 왼쪽에서 오른쪽(→)방향, 오른쪽에서 왼쪽(←)방향을 번갈아가면서, 
       i행의 첫번째 혹은 마지막 미네랄'x'을 하나씩 제거한다.
    2. 이때 클러스터가 2개로 나누어질 수 있다. 공중에 떠 있으면 중력이 작용한다. 
    
    초기상태          6행 → 이동 후     6행 ← 이동 후      4행 → 이동 후     3행 ← 이동 후     1행 → 이동 후
    8 | ........    8 | ........    8 | ........    8 | ........    8 | ........    8 | ........
    7 | ........    7 | ........    7 | ........    7 | ........    7 | ........    7 | ........
    6 | ...x.xx.    6 | .....xx.    6 | .....x..    6 | .....x..    6 | ........    6 | ........
    5 | ...xxx..    5 | ...xxx..    5 | ...xxx..    5 | ...xxx..    5 | ........    5 | ........
    4 | ..xxx...    4 | ..xxx...    4 | ..xxx...    4 | ...xx...    4 | .....x..    4 | .....x..
    3 | ..x.xxx.    3 | ..x.xxx.    3 | ..x.xxx.    3 | ..x.xxx.    3 | ..xxxx..    3 | ..xxxx..
    2 | ..x...x.    2 | ..x...x.    2 | ..x...x.    2 | ..x...x.    2 | ..xxx.x.    2 | ..xxx.x.
    1 | .xxx..x.    1 | .xxx..x.    1 | .xxx..x.    1 | .xxx..x.    1 | .xxxxxx.    1 | ..xxxxx.
    """

    for turn, row in enumerate(rows_to_remove):
        row = R - row # 실제 cave index에 맞추기
        removed = False

        # 1. 미네랄 제거
        # 홀수일 때, 왼쪽 → 오른쪽
        if turn % 2 == 0:
            for c in range(C):
                if cave[row][c] == 'x':
                    cave[row][c] = '.'
                    removed = True
                    break
        
        # 짝수일 때, 오른쪽 ← 왼쪽
        else:
            for c in range(C-1, -1, -1):
                if cave[row][c] == 'x':
                    cave[row][c] = '.'
                    removed = True
                    break
        
        if not removed:
            continue  # 미네랄을 제거 못했으면 클러스터 갱신 불필요

        # 2. 클러스터 확인 - BFS 탐색
        visited = set()
        clusters = []

        for i in range(R):
            for j in range(C):
                if cave[i][j] == 'x' and (i, j) not in visited:
                    cluster = bfs(cave, R, C, (i, j), visited)
                    clusters.append(cluster)

        # 3. 공중에 떠 있는 클러스터가 있다면 중력 적용
        for cluster in clusters:
            for r, _ in cluster:
                if r == R - 1:
                    break
            else:
                apply_gravity(cave, R, C, cluster)
                break  # 하나만 떨어뜨리는 경우만 있음
    
    # 최종 cave 상태 출력
    for row in cave:
        print(''.join(row))

if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    cave = []
    for _ in range(R):
        row = list(sys.stdin.readline().strip())
        cave.append(row)
    
    N = int(sys.stdin.readline())
    rows_to_remove = list(map(int, sys.stdin.readline().split()))
    solution(cave, R, C, N, rows_to_remove)