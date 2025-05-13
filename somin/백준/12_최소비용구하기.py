import sys
from heapq import heappush, heappop
from collections import defaultdict

def solution(n, bus_map, start, target):
    """
    Parameters:
        n (int): 도시 개수
        m (int): 버스의 개수
        bus_map (dict of int): 시작도시: [(버스비용, 도착도시)]
        start: 시작도시
        target: 도착도시
    Returns:
        int: 출발 도시에서 도착 도시까지 가는데 드는 최소 비용
    """
    dist = [float('inf')] * (n + 1) # 해당 인덱스 도시까지의 최소비용 저장
    dist[start] = 0
    pq = [(0, start)]  # (cost, start node)

    while pq:
        cost, node = heappop(pq)

        #  이미 더 짧은 경로로 방문한 적 있다면 무시
        if cost > dist[node]:
            continue

        for next_cost, next_node in bus_map[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heappush(pq, (new_cost, next_node))

    return dist[target]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    bus_map = defaultdict(list)
    for _ in range(m):
        start, end, cost = map(int, sys.stdin.readline().split())
        bus_map[start].append((cost, end))
    
    start, target = map(int, sys.stdin.readline().split())
    
    print(solution(n, bus_map, start, target))