import sys
from heapq import heapify, heappop, heappush

def solution(arr):
    """
    input: arr = 각 회의의 시작 시간과 종료 시간이 [start, end] 형태로 저장
    output: room_cnt = 필요한 회의실의 개수
    """
    heapify(arr) # 회의 [시작, 종료] 정보, 최소 힙
    room_cnt = 1 # 필요한 회의실 갯수
    end_que = [0] # 현재 진행 중인 회의들의 종료 시간을 저장하는 최소 힙
    # 모든 회의를 다 순회.
    while arr:
        start, end = heappop(arr) # 힙에서 가장 시작 시간이 빠른 회의 
        # que의 가장 일찍 끝나는 시간보다 시작시간이 큰 경우
        if end_que[0] <= start: # 해당 회의와 같은 회의실을 사용 가능한 경우
            heappop(end_que)
            heappush(end_que, end)
        else: # 같은 회의실을 사용할 수 없는 경우 > 새 회의실 필요
            room_cnt += 1
            heappush(end_que, end)
    return room_cnt

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    sol = solution(arr)
    print(sol) 