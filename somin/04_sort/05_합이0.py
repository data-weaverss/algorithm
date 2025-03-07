import sys 

'''
return 대회에 출전할 수 있는 팀을 얼마나 많이 만들 수 있는지 
조건: 세 팀원의 코딩 실력의 합이 0
'''
def solution(arr, n):
    arr.sort()
    # [-6, -5, -4, -4, 0, 1, 2, 2, 3, 7]
    ans = 0 # 팀 갯수 저장
    for i in range(n-2):
        target = -arr[i]
        left, right = i+1, n-1
        while left < right:
            s = arr[left] + arr[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else: 
                # 합이 맞는 경우: arr[left] + arr[right] == target
                # 만약 두 포인터가 같은 값을 가리킨다면,
                # 구간 내 남은 원소 수(count)에서 두 개를 뽑는 경우의 수를 더한다
                if arr[left] == arr[right]:
                    count = right - left + 1
                    ans += count * (count - 1) // 2
                    break
                else: 
                    left_val = arr[left]
                    right_val = arr[right]
                    left_count = 0
                    right_count = 0
                    # 만족하는 left, right와 같은 값이 연속해서 몇 개 있는지 카운트
                    while left < right and arr[left] == left_val: 
                        left_count += 1
                        left += 1
                    while right >= left and arr[right] == right_val:
                        right_count += 1
                        right -= 1
                    ans += left_count * right_count
    return ans

if __name__ == "__main__":
    n = int(sys.stdin.readline()) # 10
    arr = list(map(int, input().split()))
    # 2 -5 2 3 -4 7 -4 0 1 -6

    sol = solution(arr, n)
    print(sol) 