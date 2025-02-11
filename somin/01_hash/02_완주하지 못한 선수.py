# 완주하지 못한 선수 return
# 동명이인 존재
def solution(participant, completion):
    part_dict = {}
    for name in participant: # 참가자 명단 dict 생성
        part_dict[name] = part_dict.get(name, 0) + 1
    for name in completion: # 참가자 명단에서 완주자 명단 제거
        part_dict[name] -= 1
    # 명단에 남아있는 선수 = 완주하지 못한 선수
    not_completor = dict(map(reversed, part_dict.items()))[1]
    return not_completor

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    sol = solution(participant, completion)
    print(sol)
