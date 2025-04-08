# 참고: https://jhzlo.tistory.com/76

def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    
    left, right = 0, distance
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        current = 0
        removed_rocks = 0
        
        for rock in rocks:
            if rock - current < mid:
                removed_rocks += 1
            else:
                current = rock
        
        if removed_rocks <= n:
            # 남은 거리들은 모드 mid보다 크거나 같으므로
            # n보다 작을 때는 그들 중 하나를 제거하면 됨
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer

if __name__ == "__main__":
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2
    print(solution(distance, rocks, n)) #4
