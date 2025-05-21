import sys
from collections import defaultdict
from heapq import heappush, heappop

def spread(graph, nonearly_adj_cnt, node, heap=None):
    nonearly_adj_cnt[node] = 0
    for adj_node in graph[node]:
        nonearly_adj_cnt[adj_node] -= 1
        if heap:
            if nonearly_adj_cnt[adj_node] > 0:
                heappush(heap, (-nonearly_adj_cnt[adj_node], adj_node))

def solution(nodes, edges):
    """
    얼리어답터가 아닌 node들은 자신의 모든 이웃들이 얼리어답터일 때만 아이디어를 받아드림
    모든 node가 새로운 아이디어를 받아들이기 위해 필요한 최소 얼리어답터의 수를 반환
    
    2 <= nodes <= 1,000,000
    
    총 시간 복잡도: 
    핵심 아이디어: 
    """  
    adapter = set()
    nonearly_adj_cnt = defaultdict(int)
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        nonearly_adj_cnt[u] += 1
        nonearly_adj_cnt[v] += 1
    
    heap = []
    for node, adj_nodes in graph.items():
        if len(adj_nodes) == 1 and nonearly_adj_cnt[adj_nodes[0]] > 0:
            adapter.add(adj_nodes[0])
            spread(graph, nonearly_adj_cnt, adj_nodes[0])
    
    for node, adj_cnt in nonearly_adj_cnt.items():
        if adj_cnt > 0:
            heappush(heap, (-adj_cnt, node))
        
    while heap:
        value, node = heappop(heap)
        if nonearly_adj_cnt[node] != -value: continue
        if nonearly_adj_cnt[node] <= 0: continue
        adapter.add(node)
        
        spread(graph, nonearly_adj_cnt, node, heap)

    return len(adapter)
                        
                
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    
    print(solution(N, edges))
