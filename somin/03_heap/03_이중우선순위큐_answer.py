import heapq

def solution(operations):
    min_heap, max_heap = [], []
    valid = {}  # 각 원소의 유효 상태를 기록하는 딕셔너리
    idx = 0     # 각 원소에 부여할 고유 인덱스

    for op in operations:
        command, value = op.split()
        if command == "I":
            num = int(value)
            # 두 힙에 (값, 인덱스)를 삽입합니다.
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            valid[idx] = True
            idx += 1
        else:  # 삭제 연산("D")
            if value == "1":
                # 최대값 삭제: max_heap의 top이 유효한지 확인
                while max_heap and not valid.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)
                if max_heap:
                    _, del_idx = heapq.heappop(max_heap)
                    valid[del_idx] = False
            else:  # value == "-1", 최솟값 삭제
                while min_heap and not valid.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)
                if min_heap:
                    _, del_idx = heapq.heappop(min_heap)
                    valid[del_idx] = False

    # 남은 원소들 중 삭제된 항목을 건너뛰기 위한 정리 과정
    while min_heap and not valid.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    while max_heap and not valid.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    else:
        # max_heap의 최댓값은 음수로 저장되어 있으므로 부호를 뒤집어 반환합니다.
        return [-max_heap[0][0], min_heap[0][0]]

if __name__ == "__main__":
    # 예시 테스트
    operations = ["I 2", "I 1", "D 1", "I 3", "D -1"]
    print(solution(operations))  # 예상 출력: [3, 3]
