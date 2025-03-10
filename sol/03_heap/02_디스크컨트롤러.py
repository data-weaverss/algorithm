from heapq import heappush, heappop, heapify


def solution(jobs):
    """
    - 작업의 소요 시간이 짧은 것, 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높음

    - 우선순위 큐(heapq)를 활용하여 구현:
      - 요청된 작업을 저장하는 `job_queue` (요청 시간 기준 정렬)
      - 실제로 실행할 작업을 저장하는 `processing_queue` (소요 시간 기준 정렬)

    - 시간 복잡도 O(NlogN)
    """
    total_turnaround_time = 0  # 총 반환 시간

    job_queue = []  # 대기 큐(요청 시간 min heapq)
    for job_number, (arrival_time, burst_time) in enumerate(jobs):
        heappush(job_queue, (arrival_time, burst_time, job_number))

    cur_time = 0  # 현재 시간(하드디스크가 작업을 수행하는 시점)
    processing_queue = []  # 작업 처리 큐(소요 시간, 요청 시간, 작업 번호 min heapq)

    # 모든 작업이 완료될 때까지 실행
    while job_queue or processing_queue:

        # 현재 시간까지 요청된 모든 작업을 "작업 처리 큐"로 이동
        while job_queue and job_queue[0][0] <= cur_time:
            arrival_time, burst_time, job_number = heappop(job_queue)
            # 소요 시간, 요청 시간, 작업 번호 순으로 정렬 됨
            heappush(processing_queue, (burst_time, arrival_time, job_number))

        if processing_queue:
            # 처리할 작업이 있는 경우, 가장 소요 시간이 짧은 작업을 선택하여 실행
            burst_time, arrival_time, job_number = heappop(processing_queue)
            cur_time += burst_time  # 현재 시간 업데이트 (작업 수행)
            total_turnaround_time += cur_time - arrival_time  # 반환 시간 계산
        else:
            # 실행할 작업이 없으면 현재 시간을 1 증가하여 다음 작업 대기
            cur_time += 1

    return total_turnaround_time // len(jobs)


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [3, 5]]
    print(solution(jobs))
