from collections import defaultdict, deque

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1  # 시작 노드 포함

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1  # 송전탑 개수 증가

    return count  # 연결된 송전탑 개수 반환

def solution(n, wires):
    min_diff = 100  # 최소 차이 초기화 (n의 최대 크기)

    for i in range(n - 1):  # 모든 간선 하나씩 제거해보기
        # 그래프 구성 (인접 리스트)
        graph = defaultdict(list)
        for j, (v1, v2) in enumerate(wires):
            if i == j:  # 현재 제거할 간선이라면 추가하지 않음
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)

        # 한쪽 네트워크의 송전탑 개수 구하기
        first_network_size = bfs(wires[i][0], graph, n)
        second_network_size = n - first_network_size  # 전체 개수에서 빼기

        # 최소 차이 갱신
        min_diff = min(min_diff, abs(first_network_size - second_network_size))

    return min_diff

if __name__ == "__main__":
    n = 9	
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    # wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
    sol = solution(n, wires)
    print(sol) # 3