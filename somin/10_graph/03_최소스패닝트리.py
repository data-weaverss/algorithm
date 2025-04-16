import sys
from collections import defaultdict
from heapq import heappush, heappop

def solution(n, graph):
    """
    Parameters:
        - graph (Dict[int, List[Tuple[int, int]]])): 각 정점에 대해 (가중치, 인접 정점)의 리스트
    Returns:
        - 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리, 
        즉 최소 스패닝 트리의 가중치 합 (int)
    """
    visited = [False] * (n + 1)
    hq = [(0, 1)] # (가중치, 시작 노드)
    total_weight = 0

    while hq:
        cost, node = heappop(hq)

        if visited[node]:
            continue
        
        visited[node] = True
        total_weight += cost

        for next_cost, adj_node in graph[node]:
            if not visited[adj_node]:
                heappush(hq, (next_cost, adj_node))

    return total_weight

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)
    for _ in range(E):
        a, b, cost = map(int, sys.stdin.readline().split())
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    print(solution(V, graph))