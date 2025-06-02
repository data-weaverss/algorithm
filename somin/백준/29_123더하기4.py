import sys

MAX = 10001
dp = [1] * MAX  # 초기값: 모든 수를 1만 사용해서 만드는 방법은 항상 1가지

# 2를 사용하는 조합 추가
for i in range(2, MAX): 
    # i-2 숫자로 만들수 있는 경우의 수에 +2만 하면 i를 만들수 있음
    dp[i] += dp[i - 2]

for i in range(3, MAX): 
    # i-3 숫자로 만들수 있는 경우의 수에 +3만 하면 i를 만들수 있음
    dp[i] += dp[i - 3]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])