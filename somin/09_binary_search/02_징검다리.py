def solution(distance, rocks, n):
    """
    Parameters:
        - distance (int): 출발지점부터 도착지점까지의 거리
        - rocks (List[int]): 바위들이 있는 위치를 담은 배열
        - n (int): 제거할 바위의 수
    Returns:
        - 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값 (int)
    """
    
    answer = 0
    start, end = 0, distance
    rocks.sort()
    rocks.append(distance)
    
    while start <= end:
        mid = (start + end) // 2 # mid = 두 지점의 최소거리 
        
        delete_cnt = 0
        pre_rock = 0
        for rock in rocks:
            if rock - pre_rock < mid: 
                delete_cnt += 1
            else:
                pre_rock = rock

        if delete_cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

        
    return answer

if __name__ == "__main__":
    distance = 25
    rocks = [2, 14, 11, 21, 17]	
    n = 2
    print(solution(distance, rocks, n)) # 4