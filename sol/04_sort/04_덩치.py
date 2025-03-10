import sys


def solution(N, body_size):
    """
    - N : 참가자의 수
        - 참가자의 수가 2명 이상 50명 이하로 O(N^2) 시간복잡도로 해결 가능
    - body_size(list of tuples): 참가자의 몸무게와 키 정보
    """
    ranks = [0] * N

    for i in range(N):
        count = 0 # 현재 참가자보다 몸무게와 키가 모두 큰 사람 수
        for j in range(N):
            if i == j: # 자기 자신과 비교할 필요 없음
                continue
            
            # 다른 참가자의 몸무게와 키가 모두 클 경우 count 증가
            if body_size[i][0] < body_size[j][0] and body_size[i][1] < body_size[j][1]:
                count += 1

        ranks[i] = count + 1

    return ranks


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    body_size = [tuple(map(int, input().split())) for idx in range(N)]

    print(*solution(N, body_size))
