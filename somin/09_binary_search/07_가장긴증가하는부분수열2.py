import sys

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

if __name__ == "__main__":
    """
    Parameters:
        - n (int): 배열 arr의 크기
        - arr (List[int]): 수열
    Returns:
        - 수열의 가장 긴 증가하는 부분 수열의 길이 (int)
    """
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    lis_candidate = [arr[0]] # 증가 수열 저장
    for i in range(n):
        if arr[i] > lis_candidate[-1]:
            # 현재 숫자가 ascending_arr의 마지막 값보다 크다면, 
            # 그대로 이어서 증가하는 부분 수열에 추가.
            lis_candidate.append(arr[i])
        else:
            # 그렇지 않으면, 
            # 이 숫자가 들어갈 자리를 찾아서 해당 위치의 값을 교체.
            idx = binary_search(lis_candidate, arr[i])
            lis_candidate[idx] = arr[i]

    print(len(lis_candidate))

    """
    진행 과정: 예) arr = [10, 20, 10, 30, 20, 50, 11, 12]
    i = 0) [10]
    i = 1) [10, 20]
    i = 2) [10, 20] 
    i = 3) [10, 20, 30]
    i = 4) [10, 20, 30] 
    i = 5) [10, 20, 30, 50]
    i = 6) [10, 11, 30, 50] → 더 작은 수로 교체
    i = 7) [10, 11, 12, 50] → 더 작은 수로 교체

    결과: 4

    결과적으로 lis_candidate에는 실제 LIS(최장 증가 수열)는 아니지만, LIS의 길이만큼의 최적 구성 후보가 들어 있다.
    따라서 그 길이를 출력하면 가장 긴 증가하는 부분 수열의 길이가 된다.
    """