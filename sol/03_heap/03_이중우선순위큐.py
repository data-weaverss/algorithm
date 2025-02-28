from heapq import heappush, heappop, heapify
from collections import defaultdict


def clean_heap(heap, record, is_max_heap=False):
    """
    주어진 힙(heap)에서 이미 삭제된(유효하지 않은) 값을 정리하는 함수
    - is_max_heap이 True이면 최대 힙(-값 저장)으로 처리
    """
    while heap and record[-heap[0] if is_max_heap else heap[0]] <= 0:
        heappop(heap)


def solution(operations):
    min_q = []
    max_q = []
    record = defaultdict(int)  # 각 숫자의 삽입 개수를 기록하는 딕셔너리(유효성 체크용)

    for operation in operations:
        if operation.startswith("I"):
            num = int(operation.split(" ")[1])
            heappush(min_q, num)
            heappush(max_q, -num)
            record[num] += 1
        elif operation == "D 1":  # 최댓값 삭제 연산
            clean_heap(max_q, record, is_max_heap=True)
            if max_q:
                record[-heappop(max_q)] -= 1
        elif operation == "D -1":
            clean_heap(min_q, record)
            if min_q:
                record[heappop(min_q)] -= 1

    # 남은 값에서 유효하지 않은 값 정리
    clean_heap(min_q, record)
    clean_heap(max_q, record, is_max_heap=True)

    return [0, 0] if not min_q or not max_q else [-heappop(max_q), heappop(min_q)]


if __name__ == "__main__":
    operations = ["D 1", "I -45", "D 1", "D -1"]
    print(solution(operations))
