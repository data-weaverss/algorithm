def solution(people, limit):
    boat_cnt = 0
    people.sort() # 오름차순 정렬

    # min, max 합을 limit과 비교하여 구명보트 카운트
    min_idx = 0
    max_idx = len(people) - 1
    while min_idx <= max_idx:
        if people[min_idx] + people[max_idx] <= limit:
            # 두 사람이 하나의 보트를 탈 수 있는 경우
            min_idx += 1
        max_idx -= 1
        boat_cnt += 1

    return boat_cnt

if __name__ == "__main__":
    people = [70, 80, 50]
    limit = 100
    print(solution(people, limit))