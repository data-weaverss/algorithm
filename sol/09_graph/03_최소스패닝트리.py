import sys
from collections import defaultdict
from heapq import heappop, heappush

# 프림의 시간 복잡도: O(E log V)
# 크루스칼의 시간 복잡도: O(E log E)
# 그래프 내에 간선이 많은 경우는 프림 알고리즘, 
# 간선이 적은 경우는 크루스칼 알고리즘이 유리
# 이 문제에서 V는 10,000, E는 100,000이므로 프림이 더 알맞음

def solution(V, E, edges):
    """
    정점의 개수 V, 간선의 개수 E, 간선 정보 edges가 주어질 때,
    최소 스패닝 트리를 출력
    """
    graph  = defaultdict(list)
    for v1, v2, cost in edges:
        graph[v1].append((v2, cost))
        graph[v2].append((v1, cost))
    
    min_heap = [(0, 1)]  # (cost, vertex)
    visited = [False] * (V + 1)
    mst = 0
    
    while min_heap:
        cost, vertex = heappop(min_heap)
        if visited[vertex]:
            continue
        visited[vertex] = True
        mst += cost

        for neighbor, edge_cost in graph[vertex]:
            if not visited[neighbor]:
                heappush(min_heap, (edge_cost, neighbor))
    
    print(mst)
                    
if __name__ == "__main__":
    input = sys.stdin.readline
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    solution(V, E, edges)