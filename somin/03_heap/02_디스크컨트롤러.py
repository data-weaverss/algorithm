import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 요청 시각 기준 정렬
    n = len(jobs)
    waiting = []  # 대기 큐 (작업시간, 요청 시각)
    time = 0      # 현재 시간
    idx = 0       # jobs의 인덱스
    total_wait = 0  # 총 대기 시간

    while idx < n or waiting:
        # 현재 시각에 도착한 작업들을 waiting 큐에 삽입
        while idx < n and jobs[idx][0] <= time:
            start, duration = jobs[idx]
            heapq.heappush(waiting, (duration, start))
            idx += 1
        
        # 대기 큐에 작업이 있다면 작업 처리
        if waiting:
            duration, start = heapq.heappop(waiting)
            time += duration  # 작업 완료 시간 갱신
            total_wait += (time - start)  # 대기 시간 = (작업 완료 시간 - 요청 시각)
        else:
            # 현재 진행할 작업이 없으면, 다음 작업의 시작 시각으로 시간 점프
            time = jobs[idx][0]
    
    return total_wait // n  # 평균 대기 시간을 정수로 반환

if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [3, 5]]
    sol = solution(jobs)
    print(sol)  # 출력: 8
