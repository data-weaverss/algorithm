import sys
from collections import defaultdict
from heapq import heappush, heappop
import pprint

def dijkstra(graph, N, start):
    """T(2번 정점)에서 모든 정점까지 최단 거리 계산 (다익스트라 알고리즘)"""
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, node = heappop(pq)
        if dist[node] < cost:
            continue
        for w, adj in graph[node]:
            if dist[adj] > cost + w:
                dist[adj] = cost + w
                heappush(pq, (dist[adj], adj))

    return dist

def solution(graph, N, dist):
    """
    정점 S (1번)에서 정점 T (2번)로 이동하는 합리적인 이동경로 개수 계산
    - 이동 조건: 현재 정점에서 T까지의 최단 거리 > 다음 정점에서 T까지의 최단 거리
    
    S에서 T까지 이동하면서 합리적인 이동경로 조건을 만족하는 경로만 탐색
    """
    dp = [0] * (N + 1)
    dp[2] = 1  # 도착 정점은 경로 수 1로 시작

    # 거리 오름차순으로 정점 정렬 (거리가 가까운 정점부터)
    order = sorted(range(1, N + 1), key=lambda x: dist[x])

    for u in order:
        for d, v in graph[u]:
            if dist[u] > dist[v]:  # T까지 더 가까운 정점으로만 이동
                dp[u] += dp[v]

    return dp[1]  # 시작 정점 S=1의 경로 수 반환

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)
    for _ in range(M):
        u, v, d = map(int, sys.stdin.readline().split())
        graph[u].append([d, v])
        graph[v].append([d, u])
    
    dist = dijkstra(graph, N, 2)  # T=2에서 모든 정점까지 최단거리 계산
    result = solution(graph, N, dist)
    print(result)