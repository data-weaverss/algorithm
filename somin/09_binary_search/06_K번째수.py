import sys

def solution(n, k):
    """
    Parameters:
        - n (int): 2차원 배열 A의 크기
        - k (int): 찾고 싶은 일차원 배열 B의 위치
    Returns:
        - B를 오름차순 정렬했을 때, B[k]를 구해보자. (int)
    """
    left, right = 1, n*n

    while left <= right:
        mid = (left + right) // 2

        # A[i][j] <= x인 값의 개수 계산
        '''
        [[1, 2, 3], → n -> mid//1 = 6
         [2, 4, 6], → 2n -> mid//2 = 3
         [3, 6, 9]] → 3n 
        '''
        less_cnt = 0
        for i in range(1, n+1): # 1행부터 n행까지
            less_cnt += min(mid // i, n) # 한 행에 최대 n개
        
        if less_cnt < k:
            left = mid + 1
        else: 
            answer = mid
            right = mid - 1

    return answer

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())

    print(solution(n, k))