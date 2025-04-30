import sys
from collections import defaultdict, deque
from heapq import heappush, heappop

def solution(graph, target, n, build_time):
    """
    Parameters:
        - graph (Dict[int, List[Tuple[int, int]]])): 각 정점에 대해 (가중치, 인접 정점)의 리스트
        - target(int): 목표 건물
        - build_time (List[int]): 건물 건설 시간
    Returns:
        - 특정건물(target)을 가장 빨리 지을 때까지 걸리는 최소시간 (int)
    """
    indegree = [0] * (n + 1) # 진입 차수
    dp = [0] * (n + 1) # i 건물까지 건설하는 데 걸리는 최소 시간

    # 진입 차수 계산
    for u in range(1, n+1):
        for v in graph[u]:
            indegree[v] += 1

    queue = deque()

    # 진입 차수가 0인 노드부터 시작
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = build_time[i - 1] # 해당 건물 건설 시간만 필요함

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            indegree[next_node] -= 1
            # 선행 건물이 모두 완성되어야 함
            dp[next_node] = max(dp[next_node], dp[node] + build_time[next_node - 1])
            if indegree[next_node] == 0:
                queue.append(next_node)

    return print(dp[target])


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, k = map(int, sys.stdin.readline().split())
        build_times = list(map(int, sys.stdin.readline().split()))
        
        graph = defaultdict(list)
        for _ in range(k):
            x, y = map(int, sys.stdin.readline().split())
            graph[x].append(y)

        target = int(sys.stdin.readline())
        solution(graph, target, n, build_times)
