from collections import defaultdict
from heapq import heappush, heappop

def solution(n, costs):
    """
    Args:
        - n : n개의 섬
        - costs : 각 섬을 연결하는 비용
    Returns:
        - answer : 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용
    """
    graph = defaultdict(list)
    total_cost = 0
    
    for cur_node, adjacent, cost in costs: # 양방향으로 간선 추가
        graph[cur_node].append((adjacent, cost))
        graph[adjacent].append((cur_node, cost))
    
    mst = [] # (cost, 연결된 정점)
    heappush(mst, (0, next(iter(graph)))) # 시작 정점
    
    visited = [False] * n # 방문 여부
    
    while mst:
        cost, cur = heappop(mst)
        
        if visited[cur]:
            continue
        
        visited[cur] = True
        total_cost += cost
        
        # 현재 정점과 연결된 모든 간선을 우선순위 큐에 추가
        for adjacent, node_cost in graph[cur]:
            if not visited[adjacent]:
                heappush(mst, (node_cost, adjacent))
    
    return total_cost
    

if __name__ == "__main__":
    n = 6
    costs = [[0,1,8],[1,2,2],[2,3,1],[2,4,3],[3,4,1], [3,5,8]]
    print(solution(n, costs)) # 22