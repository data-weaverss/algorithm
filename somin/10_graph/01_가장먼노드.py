from collections import deque, defaultdict

def solution(n, edge):
    """
    Parameters:
        - n (int): 노드 수
        - edge (List[int]): 간선 정보
    Returns:
        - 1번 노드로부터 가장 멀리 떨어진 노드의 개수(int)
    """
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    '''
    {
    3: [6, 4, 2, 1], 
    6: [3], 
    4: [3, 2], 
    2: [3, 1, 4, 5], 
    1: [3, 2], 
    5: [2]
    }
    '''
    visited = set([1])  # 시작점 방문 처리
    queue = deque([(1, 0)]) # 노드번호, 거리
    
    longest_dist = 0
    answer = 0

    while queue:
        cur_node, cur_dist = queue.popleft()

        if cur_dist > longest_dist:
            longest_dist = cur_dist
            answer = 1
        elif cur_dist == longest_dist:
            answer += 1

        for adj_node in graph[cur_node]:
            if adj_node not in visited:
                visited.add(adj_node)
                queue.append((adj_node, cur_dist + 1))

    return answer

if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))