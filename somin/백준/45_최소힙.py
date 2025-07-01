import sys
from heapq import heappop, heappush

def solution(input_nums):
    """
    다음 입력에 따라 처리 (최소 힙 이용)
    1. 자연수 x : 배열에 자연수 x 삽입
    2. 0      : 배열에서 min 값 출력하고 제거
    """
    heap = []
    for num in input_nums:
        if num > 0:
            heappush(heap, num)
        elif heap:
            min_num = heappop(heap)
            print(min_num)
        else:
            print(0)

if __name__ == "__main__":
    N = int(sys.stdin.readline()) 
    input_nums = [int(sys.stdin.readline()) for _ in range(N)]

    solution(input_nums, N)