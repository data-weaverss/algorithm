import sys

def solution(n, s, numbers):
    """
    Parameters:
        n (int): 수열의 길이
        s (int): 합 기준
        numbers (list of int): 수열
    Returns:
        int: 연속된 부분 수열 중 합이 s 이상인 가장 짧은 길이 (없으면 0)
    """
    left = 0        # 부분합의 시작 인덱스
    current_sum = 0 # 현재 부분합
    min_length = float('inf') # 최소 길이

    # 오른쪽 끝 인덱스를 확장하면서 부분합 갱신
    for right in range(n):
        current_sum += numbers[right]

        # 부분합이 s 이상인 경우, 왼쪽 인덱스를 이동시켜 길이 최소화 시도
        while current_sum >= s:
            min_length = min(min_length, right - left + 1)
            current_sum -= numbers[left]
            left += 1

    return 0 if min_length == float('inf') else min_length

if __name__ == "__main__":
    n, s = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    
    print(solution(n, s, numbers))