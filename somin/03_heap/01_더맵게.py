import heapq

def solution(scoville, K):
    mix_cnt = 0
    min_heap = []
    for s in scoville:
        heapq.heappush(min_heap, s)
    
    # 최댓값이 K 미만이 아닐때까지
    while min_heap[0] < K:
        # 모든 음식 스코빌 >= K 가 될 수 없을 때
        if len(min_heap) == 1: 
            return -1
        # 모든 음식 스코빌 >= K
        first = heapq.heappop(min_heap)
        second = heapq.heappop(min_heap)

        # 음식 섞고 해당 스코빌 계산
        heapq.heappush(min_heap, first + second * 2)
        mix_cnt += 1

    return mix_cnt

if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    sol = solution(scoville, K)
    print(sol) # 출력: 2