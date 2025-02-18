from collections import deque
import math


# progresses: 각 작업의 진도
# speeds: 각 작업의 개발 속도
# return 각 배포마다 몇 개의 기능이 배포되는지
def solution(progresses, speeds):
    if not progresses:  # progresses가 비어있으면
        return []

    answer = []
    q = deque()  # 작업 완료까지 필요한 날짜를 저장하는 큐

    # 각 작업의 완료 예상일을 계산하여 큐에 추가
    for p, s in zip(progresses, speeds):
        q.append(math.ceil((100 - p) / s))

    batch_count = 1  # 현재 배포에서 포함된 기능 개수
    first_task_days = q.popleft()  # 첫 번째 작업의 완료 예상일
    while q:
        next_task_days = q.popleft()
        if next_task_days <= first_task_days:
            batch_count += 1
        else:
            answer.append(batch_count)  # 이전 배포 개수 저장
            # 새로운 배포 시작
            first_task_days = next_task_days
            batch_count = 1

    # 마지막 배포 그룹 추가
    return answer + [batch_count]


if __name__ == "__main__":
    progresses = [95, 95, 95, 20]
    speeds = [4, 4, 6, 20]
    sol = solution(progresses, speeds)
    print(sol)
