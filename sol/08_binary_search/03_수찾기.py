import sys

def solution(N, A_list, numbers):
    """
    numbers 에 있는 숫자들이 A_list에 있는지 출력
    """
    A_list.sort()
    
    for number in numbers:
        start, end = 0, N - 1
        exist = 0
        while start <= end:
            mid = (start + end) // 2
            if A_list[mid] == number:
                exist = 1
                break
            elif A_list[mid] > number:
                end = mid - 1
            else:
                start = mid + 1
        
        print(exist)
    
if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    A_list = list(map(int, input().split()))
    M = int(input())
    numbers = list(map(int, input().split()))

    solution(N, A_list, numbers)