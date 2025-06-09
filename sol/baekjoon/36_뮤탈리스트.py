import sys
from collections import defaultdict
from itertools import permutations

def solution(svc_count, svcs):
    """
    모든 svc를 파괴하기 위해 공격해야 하는 최소 횟수 반환

    1 <= svc_count <= 3,
    1 <= svc <= 60
    
    총 시간 복잡도: O(3! * 61^3) =  O(10^6)
    핵심 아이디어: 
        - BFS를 이용한 상태 공간 탐색 (각 단계별 가능한 모든 상태 추적)
        - 각 공격은 서비스별 다른 피해량 적용 (순열을 이용한 조합 생성)
        - DP를 통해 단계별 상태 저장으로 중복 계싼 방지
    """ 
    # DP 초기화: key=공격 횟수, value=가능한 서비스 상태 집합
    dp = defaultdict(set)
    dp[0].add(tuple(svcs))
    
    # 가능한 모든 공격 조합 생성 
    # 3개 서비스인 경우 (-9, -3, -1)의 모든 순열 생성
    adds = set(permutations([-(3**(2-i)) for i in range(svc_count)], svc_count))
    answer = 0 # 최소 공격 횟수 카운터

    while True:
        # 현재 공격 횟수에서 가능한 모든 상태 순회
        for cand in dp[answer]:
            # 모든 서비스 체력 0 이하 확인
            for idx in range(svc_count):
                if cand[idx] > 0:
                    break
                if idx == svc_count - 1:
                    return answer
                
            for add in adds:
                # 각 서비스에 순열 조합 적용 후 새 상태 계산
                dp[answer + 1].add(tuple([cand[i] + add[i] for i in range(svc_count)]))
        answer += 1

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    SVC = list(map(int, input().split()))
    
    print(solution(N, SVC))
