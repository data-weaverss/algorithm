from heapq import heapify, heappop, heappush

def solution(operations):
    min_heap, max_heap = [], []
    valid = {} # 값의 존재 유무 → True/False
    length = 0 # 힙의 길이

    for operation in operations:
        # 현재 저장된 원소가 없으면 힙 초기화
        if length == 0:
            min_heap, max_heap = [], []

        command, value = operation.split(' ')
        value = int(value)

        if command == "I": # 삽입
            heappush(min_heap, value)
            heappush(max_heap, -value)
            valid[value] = True
            length += 1

        elif length > 0: # 삭제
            if value == -1:  # 최솟값 삭제
                removed = heappop(min_heap)
            else:  # 최댓값 삭제
                removed = -heappop(max_heap)
            if removed in valid:
                del valid[removed]
            length -= 1

    answer = []
    # 힙에서 유효한 값을 찾는 함수 
    while max_heap:
        max_neg = max_heap[0]
        max_value = -max_neg
        # 현재 problems에 존재하고 난이도가 일치하면 유효
        if max_value in valid:
            answer.append(max_value)
            break
        else:
            heappop(max_heap)
    if len(answer) != 1:
        answer.append(0)

    while min_heap:
        min_value = min_heap[0]
        if min_value in valid:
            answer.append(min_value)
            break
        else:
            heappop(min_heap)
    if len(answer) != 2:
        answer.append(0)
    
    return answer


if __name__ == "__main__":
    operations = ["I 16", "I -16", "D -1", "I 123", "D 1"] 
    sol = solution(operations)
    print(sol)  # 출력: [16, 16]

"""
프로그래머스에서 정답으로 나왔지만, 
이 코드는 같은 수에 대해서 유효성을 판단하지 못한다는 단점이 있음 
> 수정한다면 인덱스를 부여하는 방식으로 처리해야 할듯..
반례: ["I 16", "I 16", "D -1", "I 123", "D 1"] 
"""