def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: 
                triangle[i][j] += triangle[i-1][0]
                continue
            if j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][-1]
                continue
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle)) # 30