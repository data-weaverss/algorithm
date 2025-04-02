def solution(n, computers):
    """
    input:
        n: 컴퓨터(노드)의 수
        computers: 인접 행렬 형태의 연결 정보 (n x n)
    return: 
        연결된 네트워크의 개수
    """
    stack = [0]
    visited = set([0])  # 방문한 노드 저장
    network_cnt = 1     # 네트워크 개수 초기화

    while stack:
        curr_node = stack.pop()

        for adj_node in range(n):
            # 연결 노드(1)이며, 방문하지 않은 경우
            if computers[curr_node][adj_node] == 1 and adj_node not in visited:
                visited.add(adj_node)
                stack.append(adj_node)

        if not stack:
            # 방문하지 않은 노드가 있다면 새로운 네트워크 탐색 시작
            unvisited = set(range(n)) - visited
            if unvisited:
                next_node = unvisited.pop()
                stack.append(next_node)
                visited.add(next_node)
                network_cnt += 1
            
    return network_cnt

if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    
    print(solution(n, computers)) # 2 