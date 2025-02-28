import sys
from heapq import heappush, heappop, heapify


def solution(N, meetings):
    """
    - param N: 회의 개수
    - param meetings: (시작 시간, 종료 시간) 튜플 리스트
    - return: N개의 회의를 모두 진행할 수 있는 최소 회의실 개수
    """
    heapify(meetings)
    start_heap = meetings  # 시작 시간을 기준으로 정렬된 회의 리스트 (최소 힙)
    end_heap = []  # 현재 진행 중인 회의의 종료 시간을 저장하는 최소 힙

    while start_heap:
        # 가장 빠른 시작 시간을 가진 회의 꺼내기
        start_time, end_time = heappop(start_heap)

        # end_heap[0] -> 가장 빨리 끝나는 회의의 종료 시간
        # start_time -> 새롭게 시작할 회의의 시작 시간
        # 가장 빨리 끝나는 회의의 종료 시간 <= 새로운 회의 시작 시간
        # -> 기존 회의실을 그대로 사용할 수 있다는 뜻
        if end_heap and end_heap[0] <= start_time:
            heappop(end_heap)  # 종료된 회의 제거

        # 새 회의 추가 (종료 시간을 기준으로 정렬)
        heappush(end_heap, end_time)

    # 예제 시뮬레이션:
    # 입력: [(1, 5), (2, 6), (3, 7), (8, 9)]
    # 1. (1,5) 추가 -> end_heap = [(5,1)]  (회의실 1개 필요)
    # 2. (2,6) 추가 -> end_heap = [(5,1), (6,2)]  (회의실 2개 필요, 겹침)
    # 3. (3,7) 추가 -> end_heap = [(5,1), (6,2), (7,3)]  (회의실 3개 필요, 겹침)
    # 4. (8,9) 추가 -> (5, 1)의 회의와 안 겹쳐서 회의실 이어 받음
    # end_heap = [(6,2), (7,3), (9, 8)] 총 회의실 3개
    return len(end_heap)


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(N)]

    print(solution(N, meetings))
