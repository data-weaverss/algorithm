# 우선순위 디스크 컨트롤러를 사용한 작업을 처리할 때
# 모든 작업의 요청~작업완료까지의 시간 평균 return
import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 요청 시각 기준 정렬
    num_jobs = len(jobs) # 작업 수

    waiting_jobs = []  # 대기 큐 (작업시간, 요청 시각), 최소 힙
    current_time = 0  # 현재 시간
    job_idx = 0       # jobs의 인덱스
    total_wait_time = 0  # 모든 작업의 대기 시간 합

    # 모든 작업이 처리되거나 대기 큐가 비어질 때까지 반복
    while job_idx < num_jobs or waiting_jobs:
        # 현재 시각에 도착한 작업들을 대기 큐에 삽입
        while job_idx < num_jobs and jobs[job_idx][0] <= current_time:
            request_time, duration = jobs[job_idx]
            heapq.heappush(waiting_jobs, (duration, request_time))
            job_idx += 1
        
        # 대기 큐에 작업이 있다면 작업 처리
        if waiting_jobs:
            # 대기 큐에서 가장 작업 소요 시간이 짧은 작업 선택
            duration, request_time = heapq.heappop(waiting_jobs)
            current_time += duration  # 작업 완료 시간 갱신
            total_wait_time += (current_time - request_time)  # 요청~처리 시간
        else:
            # 처리할 작업이 없으면, 다음 작업의 시작 시각으로 시간 점프
            current_time = jobs[job_idx][0]
    
    return total_wait_time // num_jobs  # 평균 대기 시간을 정수로 반환

if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [3, 5]]
    sol = solution(jobs)
    print(sol)  # 출력: 8