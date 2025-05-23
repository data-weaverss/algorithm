import sys
from collections import defaultdict
import sys
from heapq import heappop, heappush

def solution(nodes_num, edges_num, edges):
    """
    S -> T 
    이동할 때 T에 가까워지며 이동 = 합리적인 이동경로
    그래프가 주어졌을 때 가능한 합리적인 이동경로의 개수를 반환
    S = 1, T = 2 
    
    1 <= nodes_num <= 1,000
    1 <= edges_num <= 100,000
    0 <= cost <= 10,000
    
    총 시간 복잡도: 다익스트라 O(edges_num log nodes_num) + dfs O(nodes_num + edges_num)
    핵심 아이디어: 최단 거리 구하기 - 다익스트라, dfs + 메모이제이션(top down)
    """  
    distance = [float('inf')] * (nodes_num + 1) 
    distance[2] = 0 # 도착지 2부터 모든 노드까지의 최단 경로를 저장
        
    graph = defaultdict(list)
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))
    
    pq = [(0, 2)] # 누적 거리, 노드
    
    while pq:
        dist, now = heappop(pq) 
        if distance[now] < dist:
            continue
        for nxt, cost in graph[now]: 
            new_cost = dist + cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heappush(pq, (new_cost, nxt))

    # dp[node] = node서 시작해서 T까지 도달할 수 있는 합리적인 이동경로
    dp = [-1] * (nodes_num + 1)
    
    def dfs(node):
        if node == 2: # T에 도착하여 경로 하나 완료
            return 1
        if dp[node] != -1: # 이미 계산된 경우는 바로 반환
            return dp[node]
        
        dp[node] = 0
        for nxt, _ in graph[node]:
            if distance[node] > distance[nxt]:  # T에 가까워지는 방향만 허용
                dp[node] += dfs(nxt)
        return dp[node]
    
    return dfs(1)
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(M)]
    
    print(solution(N, M, edges))
