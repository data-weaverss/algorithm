import sys
from collections import defaultdict, deque

def solution(graph, n):
    """ 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다."""
    # 진입 차수 계산
    indegree = [0] * (n+1)
    for u in range(1, n+1):
        for v in graph[u]:
            indegree[v] += 1
    
    queue = deque()
    # 진입차수 0인 것부터
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    # 줄 세우기        
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)

        for adj_node in graph[node]:
            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                queue.append(adj_node)
    
    return order

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)

    print(*solution(graph, N))