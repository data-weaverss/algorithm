import sys
from collections import defaultdict, deque
import pprint

def solution(graph, node_count):
    """
    Strahler 순서를 계산하는 함수
    - graph: 방향 그래프 (dict)
    - node_count: 노드 개수
    """
    # 진입 차수 초기화
    indegree = [0] * (node_count + 1)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    # Strahler 정보: [order, max_order_from_parents, count_of_max_order]
    strahler_info = [[0, 0, 0] for _ in range(node_count + 1)]

    # 근원 노드 큐에 추가
    queue = deque()
    for node in range(1, node_count + 1):
        if indegree[node] == 0:
            strahler_info[node][0] = 1
            queue.append(node)
    
    # 위상 정렬 + Strahler 순서 계산
    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            indegree[next_node] -= 1

            # 현재 노드의 Strahler 순서를 이용해 갱신
            curr_order = strahler_info[node][0]
            if strahler_info[next_node][1] < curr_order:
                strahler_info[next_node][1] = curr_order
                strahler_info[next_node][2] = 1
            elif strahler_info[next_node][1] == curr_order:
                strahler_info[next_node][2] += 1

            # 진입 차수가 0이 되면 최종 Strahler 순서 결정
            if indegree[next_node] == 0:
                max_order = strahler_info[next_node][1]
                count = strahler_info[next_node][2]
                if count >= 2:
                    strahler_info[next_node][0] = max_order + 1
                else:
                    strahler_info[next_node][0] = max_order
                queue.append(next_node)

    # 마지막 노드가 도착점이 아닐 수도 있으므로, 가장 큰 번호를 반환
    return max(info[0] for info in strahler_info)

if __name__ == "__main__":
    T = int(sys.stdin.readline()) # 테스트 케이스
    for _ in range(T):
        # 테스트 케이스 번호, 노드 수, 간선 수
        case_num, node_count, edge_count = map(int, sys.stdin.readline().split())
        
        graph = defaultdict(list)
        for _ in range(edge_count):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)

        order = solution(graph, node_count)
        print(f'{case_num} {order}')