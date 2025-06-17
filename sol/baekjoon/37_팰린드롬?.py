import sys

def solution(nums_len, nums, questions_len, questions):
    """ 
    nums[questions[0]-1:questions[1]] 이 팰린드롬인지  
    
    1 <= nums_len <= 2,000, 
    1 <= num <= 10^5 1 <= questions_len <= 10^6  
    
    총 시간 복잡도: O(2000^2 + 10^6)
    핵심 아이디어: DP 테이블로 구간 팰린드롬 여부를 미리 저장
    """
    # DP 테이블: dp[i][j] = i번째부터 j번째까지 수열이 팰린드롬이면 1, 아니면 0
    dp = [[0] * nums_len for _ in range(nums_len)]
    
    # 길이 1인 경우 (항상 팰린드롬)
    for i in range(nums_len):
        dp[i][i] = 1
    
    # 길이 2인 경우 (두 수가 같을 때만 팰린드롬)
    for i in range(nums_len-1):
        if nums[i] == nums[i+1]:
            dp[i][i+1] = 1
    
    # 길이 3 이상인 경우 (점화식 적용)
    for length in range(3, nums_len+1):
        for i in range(nums_len - length + 1):
            j = i + length - 1
            if nums[i] == nums[j] and dp[i+1][j-1]:
                dp[i][j] = 1
    
    for s, e in questions:
        print(dp[s-1][e-1])

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    M = int(input())
    SE = [list(map(int, input().split())) for _ in range(M)]
    solution(N, nums, M, SE)
