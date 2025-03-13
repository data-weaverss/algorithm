from itertools import permutations

def solution(k, dungeons):
    """
    - 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"
    - 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"
    
    - 던전을 최대한 많이 탐험하려고 함.
    
    - k : 유저의 현재 피로도
    - dungeons : 각 던전별 "최소 필요도 피로도", "소모 피로도" 
    - return 탐험할 수 있는 최대 던전 수
    """
    
    for i in range(1, len(dungeons) + 1):
        for perm in permutations(dungeons, i):
            cur_fatigue = k
            for (min_fatigue, consume_fatigue) in perm:
                if min_fatigue > cur_fatigue:
                    break
                cur_fatigue -= consume_fatigue
            else:
                answer = i
                break
    
    return answer

if __name__ == "__main__":
    k = 80
    dungeons = [[80, 20], [50, 40], [30, 10]]
    print(solution(k, dungeons)) 
