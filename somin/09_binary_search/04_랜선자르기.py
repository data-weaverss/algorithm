import sys

def solution(k, n, cables):
    """
    Parameters:
        - k (int): 이미 가지고 있는 랜선의 개수
        - n (int): 필요한 랜선의 개수
        - cables (List[int]): k개의 랜선 
    Returns:
        - n개의 랜선을 만들 수 있는 최대 랜선의 길이 (int)
    """
    answer = 0
    left, right = 1, max(cables)

    while left <= right:
        mid = (left + right) // 2

        cables_cnt = 0
        for c in cables:
            cables_cnt += c // mid

        if cables_cnt < n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer

if __name__ == "__main__":
    k, n = map(int, sys.stdin.readline().split())

    cables = []
    for i in range(k):
        cables.append(int(sys.stdin.readline()))
        
    print(solution(k, n, cables))