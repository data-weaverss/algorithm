def solution(n, times):
    """
    Parameters:
        - n (int): 입국심사를 기다리는 사람 수
        - times (List[int]): 각 심사관이 한 명을 심사하는 데 걸리는 시간
    Returns:
        - 모든 사람이 심사를 받는 데 걸리는 시간의 최솟값 (int)
    """

    # 최소 시간: 1분 / 최대 시간: 가장 빠른 심사관이 모두 심사할 경우
    left, right = 1, min(times) * n
    answer = -1  # 최솟값을 갱신하며 저장할 변수

    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간동안 심사 가능한 사람 수 계산
        people = 0
        for time in times:
            people += mid // time
        
        # 목표 인원 이상을 처리할 수 있는 경우, 더 짧은 시간도 가능한지 확인
        if people >= n:
            answer = mid
            right = mid - 1
        else: # 인원이 부족한 경우 → 시간 더 필요
            left = mid + 1

    return answer

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times)) # 28