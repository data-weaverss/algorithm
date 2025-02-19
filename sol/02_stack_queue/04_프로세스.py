from collections import deque


def solution(priorities, location):
    # 실행되는 순서 카운트
    answer = 0

    # 우선순위 낮은 순대로 정렬(스택의 역할) - O(N log N)
    # 마지막 요소의 우선순위가 가장 높음
    priorities_sorted = sorted(priorities)

    # 실행 대기 큐 순서와 우선순위를 저장하는 큐 초기화(인덱스, 우선순위)
    queue = deque(enumerate(priorities))

    while queue:
        idx, p = queue.popleft()

        if p == priorities_sorted[-1]:
            answer += 1
            priorities_sorted.pop()

            if idx == location:
                return answer
        else:
            queue.append((idx, p))


if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))
