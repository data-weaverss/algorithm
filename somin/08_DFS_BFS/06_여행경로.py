from collections import defaultdict
def solution(tickets):
    # 티켓 정보를 공항별로 정리하고, 사전순으로 도착지를 정렬
    graph = defaultdict(list)
    for idx, (from_airport, to_airport) in enumerate(tickets):
        graph[from_airport].append((to_airport, idx))
    for airport in graph:
        graph[airport].sort()  # 사전순 정렬
    # graph = {
    #    "ICN": [("A", 0), ("B", 1)],
    #    "B": [("ICN", 2)]
    #}

    num_tickets = len(tickets)
    visited = [False] * num_tickets
    final_path = []

    def dfs(current_airport, path):
        nonlocal final_path

        # 모든 티켓을 다 사용한 경우 → 결과 저장하고 종료
        if len(path) == num_tickets + 1:
            final_path = path[:]
            return True  # 유효한 경로 찾음 → 더 이상 탐색할 필요 없음

        # 현재 공항에서 출발 가능한 항공권 탐색
        for next_airport, ticket_idx in graph[current_airport]:
            if not visited[ticket_idx]:
                visited[ticket_idx] = True
                path.append(next_airport)

                if dfs(next_airport, path):
                    return True  # 더 이상 탐색 필요 없음

                # 백트래킹
                path.pop()
                visited[ticket_idx] = False

        return False  # 유효한 경로를 찾지 못함

    dfs("ICN", ["ICN"])
    return final_path

if __name__ == "__main__":
    # tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
    print(solution(tickets))  # # ['ICN', 'B', 'ICN', 'A']