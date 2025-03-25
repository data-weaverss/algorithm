def solution(triangle):
    """
    거쳐간 숫자의 최댓값을 return
    Top-down 방식
        [7], 
       [3, 8], 
      [8, 1, 0], 
     [2, 7, 4, 4], 
    [4, 5, 2, 6, 5]
    """
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i+1])):
            if j == 0: # 첫번째 원소
                triangle[i+1][j] += triangle[i][j]
            elif j == i+1: # 마지막 원소
                triangle[i+1][j] += triangle[i][j-1]
            else: # 그외 원소 - 상위 대각선 방향 좌우 중 큰 값 
                triangle[i+1][j] += max(triangle[i][j-1], triangle[i][j])
    return max(triangle[-1])


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle)) # 30
