from heapq import heappush, heappop, heapify


def solution(scoville, K):
    answer = 0  # 섞는 횟수

    heapify(scoville)  # 최소 힙으로 변환

    # 가장 작은 원소가 K 이상이 될 때까지 반복
    while scoville and scoville[0] < K:
        # 만약 남은 음식이 하나뿐이면 K 이상으로 만들 수 없음
        if len(scoville) == 1:
            return -1
        mixed_scoville = heappop(scoville) + 2 * heappop(scoville)

        # 새로운 음식의 스코빌 지수를 힙에 추가
        heappush(scoville, mixed_scoville)
        answer += 1

    return answer


if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 10
    print(solution(scoville, K))
