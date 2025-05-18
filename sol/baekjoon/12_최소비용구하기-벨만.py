import sys

def solution(nums_city, nums_bus, bus_map, start, end):
    """
    nums_city: 도시의 개수, nums_bus: 버스의 개수
    bus_map: 출발 도시, 도착지 도시, 버스 비용
    start 부터 end 도시까지 가는데 드는 비용의 최소 비용을 반환
    
    1 <= nums_city <= 1,000
    1 <= nums_bus <= 100,000
    0 <= 버스 비용 < 100,000
    
    총 시간 복잡도: O(10^3 * 10^5) = O(10^8)
    핵심 아이디어: 다익스트라, 벨만-포드 최단 거리 구하기
    """  
    
    dist = [float('inf')] * (nums_city + 1)
    dist[start] = 0

    for _ in range(nums_city - 1): # O(1,000)
        for u, v, cost in bus_map: # O(100,000)
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
    
    return dist[end]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    bus_map = [list(map(int, input().split())) for _ in range(M)]
    start, end = list(map(int, input().split()))
    print(solution(N, M, bus_map, start, end))
    