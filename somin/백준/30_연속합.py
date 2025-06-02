import sys

def solution(n, arr):
    cur_sum = 0 # 현재 위치까지의 연속 부분합
    max_sum = -float('inf') # 최대 연속 부분합

    for i in range(n):
        # 현재 원소를 단독으로 시작할지, 이전까지의 합에 더할지 결정
        cur_sum = max(arr[i], cur_sum + arr[i])
        max_sum = max(max_sum, cur_sum)

    return max_sum
    

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solution(n, arr))