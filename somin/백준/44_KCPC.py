import sys

"""
입력된 로그를 분석해 우리 팀(my_team)의 순위를 구하라.

- 제출 기록을 순차 처리하면서 최고 점수 갱신과 부가 정보(제출 수, 시간) 저장
- 팀별로 총점을 계산하고, 주어진 정렬 기준에 맞게 팀 정렬
- my_team의 순위를 찾아서 출력
"""
T = int(sys.stdin.readline())
for _ in range(T):
    team_cnt, problem_cnt, my_team, submit_cnt = map(int, sys.stdin.readline().split())

    # 팀별 정보 초기화
    teams = {i: {'scores': [0] * (problem_cnt + 1), 'submissions': 0, 'last_time': 0} for i in range(1, team_cnt + 1)}
    
    # 제출 로그 순차 처리
    for time in range(1, submit_cnt + 1):
        team_id, problem_no, score = map(int, sys.stdin.readline().split())

        # 문제별 최고 점수 갱신
        if score > teams[team_id]['scores'][problem_no]:
            teams[team_id]['scores'][problem_no] = score

        # 제출 횟수 증가
        teams[team_id]['submissions'] += 1
        
        # 마지막 제출 시각 갱신
        teams[team_id]['last_time'] = time

    # 팀 정렬
    sorted_teams = sorted(teams.items(), key=lambda x: (
        -sum(x[1]['scores']),  # 총점 내림차순
        x[1]['submissions'],   # 제출 횟수 오름차순
        x[1]['last_time']      # 마지막 제출 시각 오름차순
    ))

    # 내 팀 순위 출력
    for rank, (team_id, _) in enumerate(sorted_teams, start=1):
        if team_id == my_team:
            print(rank)
            break
