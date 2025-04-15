import sys

"""
1 2  3  4
2 4  6  8
3 6  9 12
4 8 12 16

k = 10
start=1, end=16, mid=8, total=4+4+2+2=12 
start=1, end=7, mid=4, total=4+2+1+1=8
start=5, end=7, mid=6, total=4+3+2+1=10 -> answer = 6
start=5, end=5, mid=5, total=4+2+1+1=8
"""
def solution(N, k):
    """
    N x N 배열 A를 일차원 배열 B에 넣고 오름차순으로 정렬 -> B[k] 출력
    """
    
    start, end = 1, N * N
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        total = sum(min(mid//i, N) for i in range(1, N + 1))
        
        if total < k:
            start = mid + 1
        elif total >= k:
            end = mid - 1
            answer = mid
    
    print(answer)
                    
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    k = int(input())

    solution(N, k)