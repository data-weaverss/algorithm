import heapq
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
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            valid[value] = True
            valid[-value] = True
            length += 1
        elif length > 0: # 삭제
            if value == -1:  # 최솟값 삭제
                removed = heapq.heappop(min_heap)
                valid[removed] = False
                valid[-removed] = False
            else:  # 최댓값 삭제
                removed = heapq.heappop(max_heap)
                valid[removed] = False
                valid[-removed] = False
            length -= 1

    # 힙에서 유효한 값을 찾는 함수 
    def search_valid(heap, valid):
        while heap:
            v = heapq.heappop(heap)
            if valid[v] == True:
                return v
        return 0
    
    max_val = -search_valid(max_heap, valid)
    min_val = search_valid(min_heap, valid)
    
    return [max_val, min_val]


if __name__ == "__main__":
    operations = ["I 16", "I -16", "D -1", "I 123", "D 1"] 
    sol = solution(operations)
    print(sol)  # 출력: [3, 3]

"""
프로그래머스에서 정답으로 나왔지만, 
이 코드는 같은 수에 대해서 유효성을 판단하지 못한다는 단점이 있음 
> 수정한다면 인덱스를 부여하는 방식으로 처리해야 할듯..
반례: ["I 16", "I -16", "D -1", "I 123", "D 1"] 
"""