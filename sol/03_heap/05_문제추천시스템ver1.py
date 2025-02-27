import sys
from heapq import heappush, heappop


def sync_heap(heap, difficulty_level):
    """
    heap과 difficulty_level이 동기화될 때까지 최상위 요소를 제거하는 함수
    - heap에서 최상위 문제의 난이도가 실제 저장된 난이도와 다르면 제거
    - 문제를 삭제하거나 난이도를 변경한 경우, 실제 저장된 난이도와 다르게 됨
    """
    while heap and difficulty_level[abs(heap[0][1])] != abs(heap[0][0]):
        heappop(heap)


def solution(difficulty_level, commands):
    easy_heap, hard_heap, result = [], [], []

    # 초기 문제들을 힙에 삽입
    for problem, difficulty in difficulty_level.items():
        heappush(easy_heap, (difficulty, problem))
        heappush(hard_heap, (-difficulty, -problem))

    # 명령어 처리
    for command in commands:
        cmd = command.split()

        if cmd[0] == "add":
            problem, difficulty = map(int, cmd[1:])
            difficulty_level[problem] = difficulty
            heappush(easy_heap, (difficulty, problem))
            heappush(hard_heap, (-difficulty, -problem))

        elif cmd[0] == "recommend":
            if cmd[1] == "1":  # 가장 어려운 문제 찾기
                sync_heap(hard_heap, difficulty_level)
                result.append(str(-hard_heap[0][1]))
            else:  # cmd[1] == '-1', 가장 쉬운 문제 찾기
                sync_heap(easy_heap, difficulty_level)
                result.append(str(easy_heap[0][1]))

        elif cmd[0] == "solved":
            difficulty_level[int(cmd[1])] = (
                0  # 해결된 문제는 난이도를 0으로 설정 -> 더이상 유효하지 않도록
            )

    return result


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    difficulty_level = {p: d for p, d in (map(int, input().split()) for _ in range(N))}
    M = int(input())
    commands = [input() for _ in range(M)]

    print("\n".join(solution(difficulty_level, commands)))
