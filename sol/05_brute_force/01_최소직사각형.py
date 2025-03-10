def solution(sizes):
    """
    - sizes: 명함의 가로, 세로 크기를 담은 2차원 배열
    - return: 모든 명함을 수납할 수 있는 지갑의 최소 크기
    """
    # 긴 변과 짧은 변의 최댓값을 저장할 변수 초기화
    long, short = 0, 0
    for size in sizes:
        # 현재 명함의 가로와 세로 중 더 긴 길이와 짧은 길이 선택
        larger, smaller = max(size), min(size)
        
        # 기존 최대 길이보다 크다면 업데이트
        if larger > long:
            long = larger
        
        # 기존 최대 짧은 길이보다 크다면 업데이트
        if smaller > short:
            short = smaller
    
    # 지갑의 최소 크기 반환 (최대 가로 * 최대 세로)
    return long * short


if __name__ == "__main__":
    sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    print(solution(sizes))
