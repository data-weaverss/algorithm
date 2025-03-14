from collections import defaultdict

def count_nodes(graph, cur_node, start_node):
    result = 0
    for neighbor in graph[cur_node]:
        if neighbor != start_node:
            # cur_node 와 start_node 사이의 간선 1개를 더함
            result += count_nodes(graph, neighbor, cur_node) + 1
            
    return result
    

def solution(n, wires):
    """
    - n: n개의 송전탑
    - wires: 연결 정보
    """
    graph = defaultdict(list)
    
    for start, end in wires:
        graph[start].append(end)
        graph[end].append(start)
        
    # 1 - 2 - 3 - 4  5, n = 5
    # 최대 n-2의 차이가 나기 때문에
    # 간선의 개수는 n-1개. 한 그룹은 n-2개, 다른 그룹은 0개
    min_difference = n - 2 
    
    for start, end in wires:
        # 특정 간선을 제거했을 때 한쪽 서브트리의 노드 개수 계산
        subtree_size = count_nodes(graph, start, end) 
        difference = abs(n-2-subtree_size*2)
        min_difference = min(min_difference, difference)
    
    return min_difference

if __name__ == "__main__":
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    print(solution(n, wires)) 
