import sys

def solution(n, m, a_arr, b_arr):
    """
    Parameters:
        - n (int): a_arr 배열의 길이
        - m (int): b_arr 배열의 길이
        - a_arr (List[int]): n개의 정수 배열
        - b_arr (List[int]): m개의 정수 배열
    Returns:
        - b_arr 배열 안에 있는 정수가 a_arr 배열에 존재유무 출력. 존재하면 1, 아니면 0 (int)
    """
    a_arr.sort()

    for target in b_arr:
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2
            
            if a_arr[mid] == target:
                print(1)
                break
            
            elif a_arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        else: print(0)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    a_arr = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    b_arr = list(map(int, sys.stdin.readline().split()))
    solution(n, m, a_arr, b_arr)