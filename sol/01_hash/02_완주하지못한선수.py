# 동명이인 처리가 핵심
def solution(participant, completion):
    participant_count = {}  # 참가자 이름별 등장 횟수를 저장할 딕셔너리

    # 참가자 수 카운트
    for p in participant:
        participant_count[p] = participant_count.get(p, 0) + 1

    # 완주한 사람들의 수 차감
    for c in completion:
        participant_count[c] -= 1

    # 완주하지 못한 사람 찾기 (값이 1 이상인 사람)
    return next(name for name, count in participant_count.items() if count > 0)


if __name__ == "__main__":
    participant = ["leo", "kiki", "eden", "kiki", "eden"]
    completion = ["eden", "kiki"]
    sol = solution(participant, completion)
    print(sol)
