# 각 배포마다 몇 개의 기능이 배포되는지를 return
# 앞 순서의 작업이 배포되어야 다음 작업도 배포할 수 있음
def solution(progresses, speeds):
    q = []
    prev_day = -1
    for progress, speed in zip(progresses, speeds):
        # 남은 작업량 처리하는 일자 계산
        work_days = (100 - progress + speed - 1) // speed # 소수점 올림

        if work_days > prev_day: # 이전 작업일보다 많으면 이전 작업 배포
            prev_day = work_days
            q.append(1)
        else:
            q[-1] += 1
        
    return q

if __name__ == "__main__":
    progresses = [95, 90, 99, 99, 80, 99] # 작업 진행률
    speeds = [1, 1, 1, 1, 1, 1] # 작업 속도
    sol = solution(progresses, speeds)
    print(sol)