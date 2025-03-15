from itertools import permutations

def solution(k, dungeons):
    """return: 유저가 탐험할수 있는 최대 던전 수"""
    max_clear = 0
    for order in permutations(dungeons):
        # 가능한 모든 탐험 순서 순회
        user_fatigue = k # 현재 남아있는 피로도
        clear_count = 0 # 현재 탐험한 던전 수
        for required, consump in order:

            if user_fatigue >= required: 
                # 던전 입장 가능
                user_fatigue -= consump
                clear_count += 1

        max_clear = max(max_clear, clear_count)

    return max_clear

if __name__ == "__main__":
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]	
    sol = solution(k, dungeons)
    print(sol) # 3